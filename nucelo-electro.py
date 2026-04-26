import rdkit as rd
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit import Chem 


def electro_nucleo_sites(mol):
    """
    Find the most electrophilic and nucleophilic site of the molecule

    Arg:
        smiles (str): SMILES string of the molecule.
    Returns:

    """
    if isinstance(mol, str):
        mol = Chem.MolFromSmiles(mol)

    rdPartialCharges.ComputeGasteigerCharges(mol)

    results = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() == 1:  # on ignore les H
            continue
        charge = atom.GetDoubleProp("_GasteigerCharge")
        results.append({
            "atom_idx": atom.GetIdx(),
            "symbol":   atom.GetSymbol(),
            "charge":   round(charge, 4),
            "type":     "electrophile" if charge > 0 else "nucleophile"
        })
        # Site le plus électrophile = charge la plus positive
    most_electrophilic = max(results, key=lambda x: x["charge"])
    
    # Site le plus nucléophile = charge la plus négative
    most_nucleophilic  = min(results, key=lambda x: x["charge"])

    print(f"Most electrophilic site: {most_electrophilic['symbol']}{most_electrophilic['atom_idx']} (charge = {most_electrophilic['charge']})")
    print(f"Most nucleophilic site:  {most_nucleophilic['symbol']}{most_nucleophilic['atom_idx']} (charge = {most_nucleophilic['charge']})")

    return most_electrophilic, most_nucleophilic 



print(electro_nucleo_sites("C[C@]12CC[C@H]3[C@@H](O)C=C[C@H]4[C@@H]3Oc5c(O)ccc(c5C4=O)[C@H]1N(CC2)C"))