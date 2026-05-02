import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from functions.functional_groups import detect_functional_groups # type: ignore
import pandas as pd #type: ignore


def detect_aromaticity(smiles: str):


    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid Molecule inserted.")

    detected_groups = detect_functional_groups(smiles)

    aromatic_atoms = []
    for atom in mol.GetAtoms():
      if atom.GetIsAromatic():
        aromatic_atoms.append(atom.GetIdx())

    aromatic_bonds = []
    for bond in mol.GetBonds():
      if bond.GetIsAromatic():
        aromatic_bonds.append((bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()))

    aromatic_rings = []
    ring_info = mol.GetRingInfo()

    for ring in ring_info.AtomRings():
      if all(mol.GetAtomWithIdx(atom_idx).GetIsAromatic() for atom_idx in ring):
        aromatic_rings.append(list(ring))

    print(f"is_aromatic: {len(aromatic_rings)} > 0")
    print(f"number_of_aromatic_rings: {len(aromatic_rings)}")
    print(f"aromatic_atoms: {aromatic_atoms}") 
    print(f"aromatic_bonds: {aromatic_bonds}")
    print(f"aromatic_rings: {aromatic_rings}")
    print(f"functional_groups: {detected_groups}")

    df_aromatic = pd.DataFrame()
    return aromatic_rings, aromatic_atoms, aromatic_bonds, detected_groups

# detect_aromaticity("CC[C@]1(C[C@@H](C2=C(C1)C(=C3C(=C2O)C(=O)C4=C(C3=O)C=CC=C4OC)O)O[C@H]5C[C@@H]([C@@H]([C@@H](O5)C)O)N)O.Cl")
