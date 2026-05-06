import rdkit as rd
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit import Chem 
from functions.functional_groups import detect_functional_groups #type: ignore
import pandas as pd #type: ignore
import streamlit as st  #type:ignore

# Table HSAB : pour chaque groupe fonctionnel
# Valeurs calibrées pour pH = 7 (environnement neutre)
# nucleo : plus négatif = meilleur nucléophile
# electro : plus positif = meilleur électrophile
 
HSAB_rules = {
    # --- NUCLÉOPHILES MOUS (polarisables) ---
    "thiol":            {"nucleo": -0.80, "electro":  0.00},  # pKa ~9 → non déprotoné à pH7
    "sulfide":          {"nucleo": -0.65, "electro":  0.00},
    "isothiocyanate":   {"nucleo": -0.50, "electro":  0.00},
 
    # --- AMINES → protonées à pH 7 (pKa conjugate acid ~9-11 > 7) → mauvais nucléophiles ---
    "primary amine":    {"nucleo":  0.10, "electro":  0.00},  # NH3+ → mauvais nucléophile
    "secondary amine":  {"nucleo":  0.10, "electro":  0.00},  # NH2+ → mauvais nucléophile
    "tertiary amine":   {"nucleo":  0.10, "electro":  0.00},  # NH+  → mauvais nucléophile
    "imine":            {"nucleo": -0.10, "electro":  0.00},  # pKa ~5-7 → partiellement protoné
 
    # --- OXYGÈNES → non déprotonés à pH 7 ---
    "alcohol":          {"nucleo": -0.55, "electro":  0.00},  # pKa ~17 → neutre à pH7
    "phenol":           {"nucleo": -0.20, "electro":  0.00},  # pKa ~9  → neutre à pH7
    "ether":            {"nucleo": -0.15, "electro":  0.00},
    "alkene":           {"nucleo": -0.20, "electro":  0.00},
 
    # --- ACIDES → carboxylic_acid déprotoné à pH 7 (pKa ~4-5 < 7 → COO-) ---
    "carboxylic_acid":  {"nucleo": -0.80, "electro":  0.30},  # COO- à pH7 → bon nucléophile
 
    # --- ÉLECTROPHILES ---
    "acyl_chloride":    {"nucleo":  0.00, "electro":  0.90},
    "anhydride":        {"nucleo":  0.00, "electro":  0.80},
    "aldehyde":         {"nucleo":  0.00, "electro":  0.70},
    "ketone":           {"nucleo":  0.00, "electro":  0.60},
    "ester":            {"nucleo":  0.00, "electro":  0.55},
    "amide":            {"nucleo":  0.25, "electro":  0.15},
    "nitro":            {"nucleo":  0.00, "electro":  0.40},
    "nitrile":          {"nucleo":  0.00, "electro":  0.50},
    "isocyanate":       {"nucleo":  0.00, "electro":  0.70},
    "alkyl halide":     {"nucleo":  0.00, "electro":  0.50},
    "epoxide":          {"nucleo":  0.00, "electro":  0.65},
    "sulfonyl chloride":{"nucleo":  0.00, "electro":  0.85},
    "sulfoxide":        {"nucleo":  0.00, "electro":  0.40},
    "sulfone":          {"nucleo":  0.00, "electro":  0.45},
    "lactone":          {"nucleo":  0.00, "electro":  0.60},
    "lactam":           {"nucleo":  0.00, "electro":  0.75},
}
 
 
def electro_nucleo_sites_hsab(mol):
    """
    Find the most electrophilic and nucleophilic sites using Gasteiger
    charges corrected by HSAB theory and functional group detection.
    Assumes neutral environment (pH = 7):
        - Amines (pKa ~9-11) are protonated → poor nucleophiles
        - Carboxylic acids (pKa ~4-5) are deprotonated → good nucleophiles (COO-)
        - Alcohols, phenols, thiols are neutral
 
    Args:
        mol (str or rdkit.Chem.Mol): SMILES string or RDKit Mol object.
 
    Returns:
        tuple: (most_electrophilic, most_nucleophilic) where each element
               is a dictionary with the following keys:
                   - atom_idx        (int)   : atom index in the molecule
                   - symbol          (str)   : atomic symbol
                   - charge          (float) : raw Gasteiger partial charge
                   - functional_group(str)   : detected functional group
                   - nuc_score       (float) : corrected nucleophilicity score
                   - elec_score      (float) : corrected electrophilicity score
                   - type            (str)   : 'electrophile' or 'nucleophile'
        
    Limitation: In molecules containing both thiol (SH) and carboxylate 
    (COO-) groups, the COO- may score higher due to its larger Gasteiger 
    charge. In practice, thiols are kinetically preferred nucleophiles 
    (soft nucleophile, HSAB theory) but this cannot be captured by 
    Gasteiger charges alone. Fukui indices (xTB) would be needed for 
    accurate prediction in such cases.              
    """
    smiles = mol if isinstance(mol, str) else Chem.MolToSmiles(mol)
    if isinstance(mol, str):
        mol = Chem.MolFromSmiles(mol)
 
    rdPartialCharges.ComputeGasteigerCharges(mol)
 
    # Détecter les groupes fonctionnels
    groups = detect_functional_groups(smiles, return_df=False)
 
    # Construire dict {atom_idx: group_name} en gardant le groupe HSAB le plus fort
    atom_to_group = {}
    for group_name, info in groups.items():
        if group_name not in HSAB_rules:
            continue
        for match in info["position"]:
            for atom_idx in match:
                if atom_idx not in atom_to_group:
                    atom_to_group[atom_idx] = group_name
                else:
                    current = HSAB_rules[atom_to_group[atom_idx]]
                    new     = HSAB_rules[group_name]
                    if (abs(new["nucleo"]) + abs(new["electro"]) >
                        abs(current["nucleo"]) + abs(current["electro"])):
                        atom_to_group[atom_idx] = group_name
 
    results = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() == 1:
            continue
 
        idx          = atom.GetIdx()
        charge       = atom.GetDoubleProp("_GasteigerCharge")
        group        = atom_to_group.get(idx, None)
        hsab         = HSAB_rules.get(group, {"nucleo": 0.0, "electro": 0.0})
        formal_charge = atom.GetFormalCharge()
 
        # Correction pour charges formelles (ex: O- ou N+)
        formal_bonus = 0.0
        if formal_charge < 0:
            formal_bonus = -0.50  # atome chargé négativement → meilleur nucléophile
        elif formal_charge > 0:
            formal_bonus =  0.50  # atome chargé positivement → moins nucléophile
 
        nuc_score  = round(charge + hsab["nucleo"]  + formal_bonus, 4)
        elec_score = round(charge + hsab["electro"], 4)
 
        results.append({
            "atom idx":         idx,
            "symbol":           atom.GetSymbol(),
            "charge":           round(charge, 4),
            "functional group": group if group else "none",
            "nuc score":        nuc_score,
            "elec score":       elec_score,
            "type":             "electrophile" if charge > 0 else "nucleophile"
        })
 
    df = pd.DataFrame(results)

    if df.empty:
        st.write("No results found.")
        return df

    most_electrophilic = df.loc[df["elec score"].idxmax()]
    most_nucleophilic  = df.loc[df["nuc score"].idxmin()]

    most_electrophilic_drop = most_electrophilic.drop(
        labels=["charge", "nuc score", "elec score"]
    )

    most_nucleophilic_drop = most_nucleophilic.drop(
        labels=["charge", "nuc score", "elec score"]
    )
 
 
    return most_electrophilic_drop, most_nucleophilic_drop

