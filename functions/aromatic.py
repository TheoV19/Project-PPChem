import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from functions.functional_groups import detect_functional_groups # type: ignore
import pandas as pd #type: ignore


# def detect_aromaticity(smiles: str):


#     mol = Chem.MolFromSmiles(smiles)

#     if mol is None:
#         raise ValueError("Invalid Molecule inserted.")

#     #detected_groups = detect_functional_groups(smiles)

#     aromatic_atoms = []
#     for atom in mol.GetAtoms():
#       if atom.GetIsAromatic():
#         aromatic_atoms.append(atom.GetIdx())

#     aromatic_bonds = []
#     for bond in mol.GetBonds():
#       if bond.GetIsAromatic():
#         aromatic_bonds.append((bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()))

#     aromatic_rings = []
#     ring_info = mol.GetRingInfo()

#     for ring in ring_info.AtomRings():
#       if all(mol.GetAtomWithIdx(atom_idx).GetIsAromatic() for atom_idx in ring):
#         aromatic_rings.append(list(ring))

#     # print(f"is_aromatic: {len(aromatic_rings)} > 0")
#     # print(f"number_of_aromatic_rings: {len(aromatic_rings)}")
#     # print(f"aromatic_atoms: {aromatic_atoms}") 
#     # print(f"aromatic_bonds: {aromatic_bonds}")
#     # print(f"aromatic_rings: {aromatic_rings}")
#     # print(f"functional_groups: {detected_groups}")
    
#     return 

aromatic_patterns = {
    # 6-membered
    'benzene':      Chem.MolFromSmarts('c1ccccc1'),
    'pyridine':     Chem.MolFromSmarts('c1ccncc1'),
    'pyrimidine':   Chem.MolFromSmarts('c1cncnc1'),
    'pyrazine':     Chem.MolFromSmarts('c1cnccn1'),
    'pyridazine':   Chem.MolFromSmarts('c1ccnnc1'),
    'triazine':     Chem.MolFromSmarts('c1ncncn1'),

    # 5-membered
    'furan':        Chem.MolFromSmarts('c1ccoc1'),
    'thiophene':    Chem.MolFromSmarts('c1ccsc1'),
    'pyrrole':      Chem.MolFromSmarts('c1cc[nH]c1'),
    'imidazole':    Chem.MolFromSmarts('c1cn[nH]c1'),
    'pyrazole':     Chem.MolFromSmarts('c1cc[nH]n1'),
    'oxazole':      Chem.MolFromSmarts('c1cnoc1'),
    'thiazole':     Chem.MolFromSmarts('c1cnsc1'),
    'isoxazole':    Chem.MolFromSmarts('c1ccon1'),
    'isothiazole':  Chem.MolFromSmarts('c1ccsn1'),
    'triazole':     Chem.MolFromSmarts('c1cn[nH]n1'),
    'tetrazole':    Chem.MolFromSmarts('c1nn[nH]n1'),

    # Fused bicyclic
    'naphthalene':  Chem.MolFromSmarts('c1ccc2ccccc2c1'),
    'indole':       Chem.MolFromSmarts('c1ccc2[nH]ccc2c1'),
    'benzimidazole':Chem.MolFromSmarts('c1ccc2[nH]cnc2c1'),
    'benzofuran':   Chem.MolFromSmarts('c1ccc2occc2c1'),
    'benzothiophene':Chem.MolFromSmarts('c1ccc2sccc2c1'),
    'quinoline':    Chem.MolFromSmarts('c1ccc2ncccc2c1'),
    'isoquinoline': Chem.MolFromSmarts('c1ccc2cnccc2c1'),
    'purine':       Chem.MolFromSmarts('c1ncc2[nH]cnc2n1'),

    # Fused polycyclic
    'anthracene':   Chem.MolFromSmarts('c1ccc2cc3ccccc3cc2c1'),
    'phenanthrene': Chem.MolFromSmarts('c1ccc2c(c1)ccc1ccccc12'),
    'acridine':     Chem.MolFromSmarts('c1ccc2nc3ccccc3cc2c1'),
}

def detect_aromatic(smiles: str) -> pd.DataFrame:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError("Invalid SMILES string.")

    results = []
    for name, pattern in aromatic_patterns.items():
        if pattern:
            matches = molecule.GetSubstructMatches(pattern)
            if matches:
                results.append({'Aromatic Group': name, 'Count': len(matches), 'Position': [list(m) for m in matches]})

    if not results:
        return pd.DataFrame([{'Aromatic Group': 'None', 'Count': 0, 'Position': []}])

    return pd.DataFrame(results)
         
