import rdkit as rd
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit import Chem 
 
def get_atom_environment(atom, mol):
    """
    Determines the chemical environment of an atom for bonus corrections.
    """
    symbol = atom.GetSymbol()
    is_aromatic = atom.GetIsAromatic()
    neighbors = [mol.GetAtomWithIdx(n.GetIdx()) for n in atom.GetNeighbors()]
    neighbor_symbols = [n.GetSymbol() for n in neighbors]
    neighbor_bonds = [mol.GetBondBetweenAtoms(atom.GetIdx(), n.GetIdx()).GetBondTypeAsDouble() 
                      for n in atom.GetNeighbors()]
 
    env = {
        "symbol": symbol,
        "is_aromatic": is_aromatic,
        "neighbors": neighbor_symbols,
        "bonds": neighbor_bonds,
    }
 
    # --- NITROGEN ---
    if symbol == "N":
        if is_aromatic:
            env["type"] = "N_aromatic"
        # Nitro group: N+ avec 2 O voisins
        elif atom.GetFormalCharge() == 1 and neighbor_symbols.count("O") >= 2:
            env["type"] = "N_nitro"
        else:
            env["type"] = "N_aliphatic"
 
    # --- OXYGEN ---
    elif symbol == "O":
        # Nitro O: voisin d'un N chargé positivement → en premier
        if any(mol.GetAtomWithIdx(n.GetIdx()).GetSymbol() == "N" and
               mol.GetAtomWithIdx(n.GetIdx()).GetFormalCharge() == 1
               for n in atom.GetNeighbors()):
            env["type"] = "O_nitro"
        # Phenolic O: attached to aromatic carbon
        elif any(mol.GetAtomWithIdx(n.GetIdx()).GetIsAromatic() 
               for n in atom.GetNeighbors()):
            env["type"] = "O_phenol"
        # Carbonyl O: double bond to C
        elif 2.0 in neighbor_bonds:
            env["type"] = "O_carbonyl"
        else:
            env["type"] = "O_alcohol"
 
    # --- SULFUR ---
    elif symbol == "S":
        env["type"] = "S"
 
    # --- CARBON ---
    elif symbol == "C":
        # Carbonyl C: double bond to O → toujours en premier
        if "O" in neighbor_symbols and 2.0 in neighbor_bonds:
            env["type"] = "C_carbonyl"
 
        elif is_aromatic:
            env["type"] = "C_aromatic"
 
        elif 2.0 in neighbor_bonds:
            # Michael acceptor: C=C adjacent to C=O
            is_michael = False
            for n in atom.GetNeighbors():
                n_atom = mol.GetAtomWithIdx(n.GetIdx())
                n_neighbors_symbols = [mol.GetAtomWithIdx(nn.GetIdx()).GetSymbol() 
                                       for nn in n_atom.GetNeighbors()]
                n_bonds = [mol.GetBondBetweenAtoms(n_atom.GetIdx(), 
                           mol.GetAtomWithIdx(nn.GetIdx()).GetIdx()).GetBondTypeAsDouble() 
                           for nn in n_atom.GetNeighbors()]
                if "O" in n_neighbors_symbols and 2.0 in n_bonds:
                    is_michael = True
                    break
            env["type"] = "C_michael" if is_michael else "C_other"
 
        else:
            env["type"] = "C_other"
 
    else:
        env["type"] = f"{symbol}_other"
 
    return env
 
 
def nucleophilicity_score(charge, env_type):
    """Lower score = better nucleophile."""
    bonus = {
        "N_aliphatic": 0.25,
        "N_aromatic":  0.05,
        "N_nitro":    -0.20,  # malus: N_nitro est électrophile
        "O_alcohol":   0.02,
        "O_phenol":    0.20,  # doublet délocalisé = mauvais nucléophile
        "O_carbonyl":  0.05,  # très mauvais nucléophile
        "O_nitro":     0.10,  # charge brute utilisée directement
        "S":           0.10,
    }
    return charge - bonus.get(env_type, 0.0)
 
 
def electrophilicity_score(charge, env_type):
    """Higher score = better electrophile."""
    bonus = {
        "C_carbonyl": 0.20,
        "C_michael":  0.08,
        "C_aromatic": 0.03,
        "N_nitro":    0.15,  # N du groupe nitro est électrophile
    }
    return charge + bonus.get(env_type, 0.0)
 
 
def electro_nucleo_sites(mol):
    """
    Find the most electrophilic and nucleophilic sites of the molecule,
    with chemical environment corrections (carbonyl, Michael acceptor,
    aromatic, aliphatic, phenol, nitro...).
 
    Args:
        mol (str or rdkit.Chem.Mol): SMILES string or RDKit Mol object.
 
    Returns:
        tuple: A tuple (most_electrophilic, most_nucleophilic) where each
               element is a dictionary with the following keys:
                   - atom_idx   (int)   : atom index in the molecule
                   - symbol     (str)   : atomic symbol (e.g. 'C', 'N', 'O')
                   - charge     (float) : raw Gasteiger partial charge
                   - env_type   (str)   : detected chemical environment
                   - nuc_score  (float) : corrected nucleophilicity score
                   - elec_score (float) : corrected electrophilicity score
                   - type       (str)   : 'electrophile' or 'nucleophile'
    """
    if isinstance(mol, str):
        mol = Chem.MolFromSmiles(mol)
 
    rdPartialCharges.ComputeGasteigerCharges(mol)
 
    results = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() == 1:  # ignore H
            continue
 
        charge = atom.GetDoubleProp("_GasteigerCharge")
        env = get_atom_environment(atom, mol)
        env_type = env["type"]
 
        results.append({
            "atom_idx":   atom.GetIdx(),
            "symbol":     atom.GetSymbol(),
            "charge":     round(charge, 4),
            "env_type":   env_type,
            "nuc_score":  round(nucleophilicity_score(charge, env_type), 4),
            "elec_score": round(electrophilicity_score(charge, env_type), 4),
            "type":       "electrophile" if charge > 0 else "nucleophile"
        })
 
    most_electrophilic = max(results, key=lambda x: x["elec_score"])
    most_nucleophilic  = min(results, key=lambda x: x["nuc_score"])
 
    print(f"Most electrophilic site: {most_electrophilic['symbol']}"
          f"{most_electrophilic['atom_idx']} "
          f"({most_electrophilic['env_type']}, "
          f"charge = {most_electrophilic['charge']}, "
          f"score = {most_electrophilic['elec_score']})")
 
    print(f"Most nucleophilic site:  {most_nucleophilic['symbol']}"
          f"{most_nucleophilic['atom_idx']} "
          f"({most_nucleophilic['env_type']}, "
          f"charge = {most_nucleophilic['charge']}, "
          f"score = {most_nucleophilic['nuc_score']})")
 
    return most_electrophilic, most_nucleophilic
 
 
print(electro_nucleo_sites("C1=CC(=CC=C1C=O)[N+](=O)[O-]"))


#paga was here