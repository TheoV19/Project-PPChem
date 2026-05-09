import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import AllChem
import py3Dmol # type: ignore
import streamlit.components.v1 as components

def draw_molecule_3d(smiles, style='stick', color='spectrum',
                     width=600, height=400, background='white', jupyter=False):
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
    view.setBackgroundColor(background)
    view.zoomTo()
    
    if jupyter:
        return view.show()
    else:
        components.html(view._make_html(), height=height)
   
    


