import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from functional_groups import detect_functional_groups
import pubchempy as pcp



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

    return {
        "is_aromatic": len(aromatic_rings) > 0,
        "number_of_aromatic_rings": len(aromatic_rings),
        "aromatic_atoms": aromatic_atoms,
        "aromatic_bonds": aromatic_bonds,
        "aromatic_rings": aromatic_rings,
        "functional_groups": detected_groups
    }

detect_aromaticity("C1=CC=NC=C1")

result = detect_aromaticity("C1=CC=NC=C1")
print(result)