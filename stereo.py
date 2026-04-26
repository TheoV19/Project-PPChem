import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D
from molecule_draw import draw2D
from rdkit.Chem import EnumerateStereoisomers
import streamlit as st


molecule = Chem.MolFromSmiles("CCCCC")  

molecule.FindPotentialStereo()








