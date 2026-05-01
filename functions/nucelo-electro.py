import rdkit as rd
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit import Chem 
from functional_groups import detect_functional_groups # type: ignore

# Table HSAB : pour chaque groupe fonctionnel
# nucleo_score : plus négatif = meilleur nucléophile
# electro_score : plus positif = meilleur électrophile

HSAB_rules = {
    # Nucléophiles mous (polarisables)
    "thiol":            {"nucleo": -0.80, "electro":  0.00},
    "sulfide":          {"nucleo": -0.65, "electro":  0.00},
    "isothiocyanate":   {"nucleo": -0.50, "electro":  0.00},

    # Nucléophiles intermédiaires
    "primary_amine":    {"nucleo": -0.60, "electro":  0.00},
    "secondary_amine":  {"nucleo": -0.45, "electro":  0.00},
    "tertiary_amine":   {"nucleo": -0.40, "electro":  0.00},
    "alcohol":          {"nucleo": -0.55, "electro":  0.00},
    "phenol":           {"nucleo": -0.25, "electro":  0.00},
    "ether":            {"nucleo": -0.15, "electro":  0.00},
    "alkene":           {"nucleo": -0.20, "electro":  0.00},
    "imine":            {"nucleo": -0.20, "electro":  0.00},

    # Électrophiles forts
    "acyl_chloride":    {"nucleo":  0.00, "electro":  0.90},
    "anhydride":        {"nucleo":  0.00, "electro":  0.80},
    "aldehyde":         {"nucleo":  0.00, "electro":  0.70},
    "ketone":           {"nucleo":  0.00, "electro":  0.60},
    "ester":            {"nucleo":  0.00, "electro":  0.55},
    "carboxylic_acid":  {"nucleo":  -0.50, "electro": 0.50},
    "amide":            {"nucleo":  0.00, "electro":  0.15},
    "nitro":            {"nucleo":  0.00, "electro":  0.40},
    "nitrile":          {"nucleo":  0.00, "electro":  0.50},
    "isocyanate":       {"nucleo":  0.00, "electro":  0.70},
    "alkyl_halide":     {"nucleo":  0.00, "electro":  0.50},
    "epoxide":          {"nucleo":  0.00, "electro":  0.65},
    "sulfonyl_chloride":{"nucleo":  0.00, "electro":  0.85},
    "sulfoxide":        {"nucleo":  0.00, "electro":  0.40},
    "sulfone":          {"nucleo":  0.00, "electro":  0.45},
    "lactone":          {"nucleo":  0.00, "electro":  0.60},
    "lactam":           {"nucleo":  0.00, "electro":  0.75},
}


def electro_nucleo_sites_hsab(mol):
    """
    Find the most electrophilic and nucleophilic sites using Gasteiger
    charges corrected by HSAB theory and functional group detection.

    Args:
        mol (str or rdkit.Chem.Mol): SMILES string or RDKit Mol object.

    Returns:
        tuple: (most_electrophilic, most_nucleophilic) dicts with keys:
                   - atom_idx   (int)
                   - symbol     (str)
                   - charge     (float)
                   - env_type   (str)
                   - nuc_score  (float)
                   - elec_score (float)
                   - functional_group (str) : groupe fonctionnel HSAB associé
    """
    smiles = mol if isinstance(mol, str) else Chem.MolToSmiles(mol)
    if isinstance(mol, str):
        mol = Chem.MolFromSmiles(mol)

    rdPartialCharges.ComputeGasteigerCharges(mol)

    # Détecter les groupes fonctionnels et leurs atomes
    groups = detect_functional_groups(smiles)

    # Construire un dict {atom_idx: (group_name, hsab_scores)}
    atom_to_group = {}
    for group_name, info in groups.items():
        if group_name not in HSAB_rules:
            continue
        for match in info["position"]:
            for atom_idx in match:
                # Garder le groupe avec le score le plus extrême
                if atom_idx not in atom_to_group:
                    atom_to_group[atom_idx] = group_name
                else:
                    # Si l'atome appartient à plusieurs groupes, garder
                    # celui avec le score HSAB le plus fort
                    current = HSAB_rules[atom_to_group[atom_idx]]
                    new     = HSAB_rules[group_name]
                    if (abs(new["nucleo"]) + abs(new["electro"]) >
                        abs(current["nucleo"]) + abs(current["electro"])):
                        atom_to_group[atom_idx] = group_name

    results = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() == 1:
            continue

        idx    = atom.GetIdx()
        charge = atom.GetDoubleProp("_GasteigerCharge")
        group  = atom_to_group.get(idx, None)
        hsab   = HSAB_rules.get(group, {"nucleo": 0.0, "electro": 0.0})
        formal_charge = atom.GetFormalCharge()
        charge_bonus = 0.0
        #Check si il y a des charges formelles (O-, )
        if formal_charge < 0:
            charge_bonus = -0.50  # Bonus massif pour un atome chargé négativement
        elif formal_charge > 0:
            charge_bonus = 0.50   # Malus pour la nucléophilie si l'atome est positif

        nuc_score = round(charge + hsab["nucleo"] + charge_bonus, 4)

        nuc_score  = round(charge + hsab["nucleo"],  4)
        elec_score = round(charge + hsab["electro"], 4)

        results.append({
            "atom_idx":        idx,
            "symbol":          atom.GetSymbol(),
            "charge":          round(charge, 4),
            "functional_group": group if group else "none",
            "nuc_score":       nuc_score,
            "elec_score":      elec_score,
            "type":            "electrophile" if charge > 0 else "nucleophile"
        })

    most_electrophilic = max(results, key=lambda x: x["elec_score"])
    most_nucleophilic  = min(results, key=lambda x: x["nuc_score"])

    print(f"Most electrophilic: {most_electrophilic['symbol']}"
          f"{most_electrophilic['atom_idx']} "
          f"({most_electrophilic['functional_group']}, "
          f"charge = {most_electrophilic['charge']}, "
          f"score = {most_electrophilic['elec_score']})")

    print(f"Most nucleophilic:  {most_nucleophilic['symbol']}"
          f"{most_nucleophilic['atom_idx']} "
          f"({most_nucleophilic['functional_group']}, "
          f"charge = {most_nucleophilic['charge']}, "
          f"score = {most_nucleophilic['nuc_score']})")

    return most_electrophilic, most_nucleophilic

print(electro_nucleo_sites_hsab("OC=C1[C@@H](O[C@H]2CC(=O)N12)C(=O)O"))

