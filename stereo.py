import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D
from molecule_draw import draw2D
from rdkit.Chem import EnumerateStereoisomers
import streamlit as st


mol = Chem.MolFromSmiles("CCCCC")  
mol_with_h = Chem.AddHs(mol)

AllChem.EmbedMolecule(mol_with_h)






