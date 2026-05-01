import rdkit as rd
import pymatgen as py
from pymatgen.core.structure import Molecule
from pymatgen.symmetry.analyzer import PointGroupAnalyzer
from rdkit import Chem 
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

def point_group (smiles):
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is None:
        raise ValueError("Invalid Molecule inserted.")
    
    mol = Chem.AddHs(mol)
    
    AllChem.EmbedMolecule(mol, AllChem.ETKDGv3())
    AllChem.MMFFOptimizeMolecule(mol)
    conf = mol.GetConformer()
    species = []
    coords = []
    
    for atom in mol.GetAtoms():
        pos = conf.GetAtomPosition(atom.GetIdx())
        species.append(atom.GetSymbol())
        coords.append([pos.x, pos.y, pos.z])
    
    molecule = Molecule(species, coords)
    analyzer = PointGroupAnalyzer(molecule)
    return analyzer.sch_symbol  

print(point_group("C"))          # methane, should be around Td
print(point_group("O"))          # water, should be around C2v
print(point_group("N"))          # ammonia, should be around C3v
print(point_group("c1ccccc1"))   # benzene, should be around D6h