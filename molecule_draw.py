import pubchempy as pcp 
import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem.Draw import IpythonConsole
IPythonConsole.ipython_useSVG=True


def draw2D(smiles: str) -> str:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES string: {smiles}")
    
    drawer = rdMolDraw2D.MolDraw2DSVG(400, 300)
    drawer.DrawMolecule(molecule)
    drawer.FinishDrawing()
    return drawer.GetDrawingText()

draw2D("CCCC")


