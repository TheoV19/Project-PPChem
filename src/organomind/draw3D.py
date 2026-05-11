from rdkit import Chem 
from rdkit.Chem import AllChem
import py3Dmol # type: ignore


# def draw_molecule_3d(smiles, style='stick', color='spectrum',
#                      width=600, height=400, background='white', jupyter=False):
#     mol = Chem.MolFromSmiles(smiles)
#     if mol is None:
#         raise ValueError(f"Invalid SMILES: {smiles}")
    
#     mol = Chem.AddHs(mol)
#     AllChem.EmbedMolecule(mol, AllChem.ETKDGv3())
#     AllChem.MMFFOptimizeMolecule(mol)
    
#     sdf_data = Chem.MolToMolBlock(mol)
    
#     view = py3Dmol.view(width=width, height=height)
#     view.addModel(sdf_data, 'sdf')
#     view.setStyle({style: {'color': color}})
#     view.setBackgroundColor(background)
#     view.zoomTo()
    
#     components.html(view._make_html(), height=height)
   
def molecule_visualization(smiles, style='stick', color='spectrum',
                    width=600, height=400, background='white'):
    """Shared logic: returns a configured py3Dmol view."""
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
    return view

def draw_molecule_3d_streamlit(smiles, style='stick', color='spectrum',
                                width=600, height=400, background='white'):
    """For Streamlit apps."""
    import streamlit.components.v1 as components
    view = molecule_visualization(smiles, style, color, width, height, background)
    components.html(view._make_html(), height=height)

def draw_molecule_3d_jupyter(smiles, style='stick', color='spectrum',
                              width=600, height=400, background='white'):
    """For Jupyter notebooks."""
    view = molecule_visualization(smiles, style, color, width, height, background)
    return view.show()


