import pubchempy as pcp 
import rdkit as rd
from rdkit import Chem 

functional_groups={
    "carboxylic_acid": "[CX3](=O)[OX2H1]",

    "ester": "[CX3](=O)[OX2H0][#6;!$(C=O)]",

    "amide": "[CX3](=O)[NX3;!$([N+])]",

    "aldehyde": "[CX3H1](=O)[#6]",

    "ketone": "[#6][CX3](=O)[#6;!$([OX2H]);!$([OX2][#6]);!$([NX3])]",

    "alcohol": "[OX2H][CX4;!$(C=O);!$([CX4][F,Cl,Br,I])]",

    "phenol": "[OX2H][c]",

    "ether": "[OD2H0]([#6;!$(C=O)])[#6;!$(C=O)]",

    "primary_amine": "[NX3;H2;!$([N+]);!$(NC=O)]([CX4])",

    "secondary_amine": "[NX3;H1;!$([N+]);!$(NC=O)]([#6])[#6]",

    "tertiary_amine": "[NX3;H0;!$([N+]);!$(NC=O)]([#6])([#6])[#6]",

    "nitrile": "[CX2]#[NX1]",

    "alkene": "[CX3;!$(C=O)]=[CX3;!$(C=O)]",

    "alkyne": "[CX2]#[CX2]",

    "benzene_ring": "[c;!$(c[OX2H])]1[c;!$(c[OX2H])][c;!$(c[OX2H])][c;!$(c[OX2H])][c;!$(c[OX2H])][c;!$(c[OX2H])]1",

    "halide": "[F,Cl,Br,I]",

    "alkyl_halide": "[CX4;!$(C=O)][F,Cl,Br,I]",

    "nitro": "[NX3+](=O)[O-]",

    "imine": "[CX3;!$(C=O)]=[NX2;!$([N+])]",

    "azide": "[NX2]=[NX2+]=[NX1-]",

    "isocyanate": "[NX2]=[CX2]=[OX1]",

    "isothiocyanate": "[NX2]=[CX2]=[SX1]",

    "thiol": "[SX2H]",

    "sulfide": "[SX2H0]([#6])[#6]",

    "sulfoxide": "[#6][SX3](=O)[#6]",

    "sulfone": "[#6][SX4](=O)(=O)[#6]",

    "sulfonamide": "[#6][SX4](=O)(=O)[NX3;!$([N+])]",

    "sulfonyl_chloride": "[#6][SX4](=O)(=O)Cl",

    "sulfonyl_fluoride": "[#6][SX4](=O)(=O)F",

    "sulfonyl_bromide": "[#6][SX4](=O)(=O)Br",

    "sulfonyl_iodide": "[#6][SX4](=O)(=O)I",

    "phosphate_ester": "[PX4](=O)([OX2][#6])([OX2H,OX2-])[OX2H,OX2-]",

    "epoxide": "[OX2r3]1[#6r3][#6r3]1",

    "acyl_chloride": "[CX3](=O)Cl",

    "anhydride": "[CX3](=O)[OX2][CX3](=O)",

    "lactone": "[CX3r](=O)[OX2r]",

    "lactam": "[CX3r](=O)[NX3r]",
}

def detect_functional_groups(smiles):
    """
    Finds functional groups if present.
    Args:
        smiles (str): SMILES string of the molecule.
    Returns:
        dict: A dictionay of detected functional groups and the amount of times.
    """
    mol = Chem.MolFromSmiles(smiles)
   
    groups_present={}
    
    if mol is None:
        raise ValueError("Invalid Molecule inserted.")

    for group, smart in functional_groups.items():
        pattern=Chem.MolFromSmarts(smart)
        matches=mol.GetSubstructMatches(pattern)
        
        if len (matches)>0:
            groups_present[group]={
                "amount": len(matches),
                "position": matches
            }
    return groups_present
    