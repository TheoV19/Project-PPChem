import rdkit as rd
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit import Chem 


def electro_nucleo_sites(mol):
    """
    Approximation simple : charge de Gasteiger
    charge > 0  → site électrophile
    charge < 0  → site nucléophile
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

    return results