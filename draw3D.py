import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D
import streamlit as st
import py3Dmol
import streamlit.components.v1 as components

def draw_molecule_3d(smiles, style='stick', color='spectrum',
                     width=600, height=400, bg_color='white'):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDGv3())
    AllChem.MMFFOptimizeMolecule(mol)
    
    sdf_data = Chem.MolToMolBlock(mol)
    
    view = py3Dmol.view(width=width, height=height)
    view.addModel(sdf_data, 'sdf')
    view.setStyle({style: {'color': color}})
    view.setBackgroundColor(bg_color)
    view.zoomTo()
    
    components.html(view._make_html(), height=height)

draw_molecule_3d('CCO')
draw_molecule_3d('c1ccccc1', style='sphere', color='blue')