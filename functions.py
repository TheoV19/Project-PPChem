import pubchempy as pcp 
import rdkit as rd
from rdkit import Chem 

functional_groups={
    "carboxylic_acid": "[CX3](=O)[OX2H1]",

    "ester": "[CX3](=O)[OX2][#6]",

    "amide": "[CX3](=O)[NX3]",

    "aldehyde": "[CX3H1](=O)[#6]",

    "ketone": "[#6][CX3](=O)[#6]",

    "alcohol": "[OX2H][CX4;!$(C=O)]",

    "phenol": "[c][OX2H]",

    "ether": "[OD2]([#6])[#6]",

    "primary amine": "[NX3;H2][CX4]",

    "secondary amine": "[NX3;H1][CX4]",

    "tertiary amine": "[NX3;H0][CX4]",

    "nitrile": "[CX2]#N",

    "alkene": "[CX3]=[CX3]",

    "alkyne": "[CX2]#[CX2]",

    "benzene_ring": "c1ccccc1",

    "halide": "[F,Cl,Br,I]",

    "nitro": "[NX3+](=O)[O-]",

    "thiol": "[SX2H]",

    "sulfide": "[SX2]([#6])[#6]",

    "sulfoxide": "[#6][SX2](=O)[#6]",

    "sulfone": "[#6][SX4](=O)(=O)[#6]",

    "phosphate": "[PX4](=O)(O)(O)[#6]",

    "epoxide": "[OX2r3]1[#6r3][#6r3]1",

    "imine": "[CX3]=[NX2]",

    "azide": "[NX2]=[NX2+]=[NX1-]",

    "isocyanate": "[NX2]=[CX2]=O",

    "isothiocyanate": "[NX2]=[CX2]=S",

    "sulfonamide": "[#6][SX4](=O)(=O)[NX3]",

    "sulfonyl chloride": "[#6][SX4](=O)(=O)Cl",

    "sulfonyl fluoride": "[#6][SX4](=O)(=O)F",

    "sulfonyl bromide": "[#6][SX4](=O)(=O)Br",

    "sulfonyl iodide": "[#6][SX4](=O)(=O)I",

    "acyl chloride": "[CX3](=O)Cl",

    "anhydride": "[CX3](=O)OC(=O)[#6]",

    "lactone": "[OX2r3]1[#6r3][#6r3]1",

    "lactam": "[NX3r3]1[#6r3][#6r3]1",

    "alkyl halide": "[CX4][F,Cl,Br,I]",
}