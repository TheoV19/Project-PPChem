import rdkit as rd
import pymatgen as py #type: ignore
from pymatgen.core.structure import Molecule #type: ignore
from pymatgen.symmetry.analyzer import PointGroupAnalyzer #type: ignore
from rdkit import Chem 
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

def find_group (smiles):
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
