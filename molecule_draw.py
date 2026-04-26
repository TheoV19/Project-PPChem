import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

def draw2D(smiles: str) -> str:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES string: {smiles}")
       
    drawer = rdMolDraw2D.MolDraw2DSVG(400, 300)
    drawer.DrawMolecule(molecule)
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
    with open("molecule.svg", "w") as f:
        f.write(svg)
    return svg

draw2D("CCC(=O)N(C1CCN(CC1)CCC2=CC=CC=C2)C3=CC=CC=C3")


#second version
#def draw(smiles: str, size=(400, 300), save_as=None):
 #   mol = Chem.MolFromSmiles(smiles)
  #  if mol is None:
   #     raise ValueError("Unexistant Smiles")
     
   # img = Draw.MolToImage(mol, size=size)
    
    #if save_as:
   #     img.save(save_as)
    #    print(f"Saved to {save_as}")
    
    #img.show()   
    #return img

#draw("CCCNNCCNNC", save_as="molecule.png")
