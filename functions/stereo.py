import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D
from molecule_draw import draw2D # type: ignore
from rdkit.Chem.EnumerateStereoisomers import EnumerateStereoisomers, StereoEnumerationOptions




def chrial_center(smiles: str)-> int:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    
    center = Chem.FindMolChiralCenters(molecule, includeUnassigned=True) #includeUnassigned=True also counts chiral center not specified in smiles
    number = len(center)
    print(f"Number of Chiral center: {number}")
    return number
    

#FindMolChiralCenter is a list of tuple: [(0, S), (3, R), (4, S)]


def color_chiral(smiles: str):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    
    stereocenters = Chem.FindMolChiralCenters(molecule, includeUnassigned=True)

    chiral_atoms = [idx for idx, _ in stereocenters] # List comprehension -> modifie des tuples de tuples en liste, _ is for stereocenter information (R or S) in tuple, here negligeable
    
    if not chiral_atoms:
        print("No chiral center found")
    else:
        print(f"Chiral centers of atoms : {chiral_atoms}")

    drawer = rdMolDraw2D.MolDraw2DSVG(400, 300)
    
    highlight_colors = {idx: (0, 1, 0) for idx in chiral_atoms}  
    
    #drawer also highlight bonds
    highlight_bond_colors: dict = {}
    highlight_bonds: list = []

    drawer.DrawMolecule(
        molecule,
        highlightAtoms=chiral_atoms,
        highlightAtomColors=highlight_colors,
        highlightBonds=highlight_bonds,
        highlightBondColors=highlight_bond_colors
    )
    
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    
    with open("molecule_chiral.svg", "w") as f:
        f.write(svg)






def find_isomers(smiles: str) -> int:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES: {smiles}")

    options = StereoEnumerationOptions(unique=True, onlyUnassigned=False, tryEmbedding=True)
    isomers = tuple(EnumerateStereoisomers(molecule, options=options))
    number = len(isomers)  
    print(f"Number of stereoisomers: {number}")
    
    return number  


smiles: str= "CC(C)C[C@@H]([C@H](CC(=O)O)O)N"

chrial_center(smiles)
color_chiral(smiles)
find_isomers(smiles)






