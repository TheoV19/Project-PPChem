functional_groups={
    "carboxylic acid": "[CX3](=O)[OX2H1]",

    "ester": "[CX3](=O)[OX2H0][#6;!$(C=O)]",

    "amide": "[CX3](=O)[NX3;!$([N+])]",

    "aldehyde": "[CX3H1](=O)[#6]",

    "ketone": "[#6][CX3](=O)[#6;!$([OX2H]);!$([OX2][#6]);!$([NX3])]",

    "alcohol": "[OX2H][CX4;!$(C=O);!$([CX4][F,Cl,Br,I])]",

    "phenol": "[OX2H][c]",

    "ether": "[OD2H0]([#6;!$(C=O)])[#6;!$(C=O)]",

    "primary amine": "[NX3;H2;!$([N+]);!$(NC=O)]([CX4])",

    "secondary amine": "[NX3;H1;!$([N+]);!$(NC=O)]([#6])[#6]",

    "tertiary amine": "[NX3;H0;!$([N+]);!$(NC=O)]([#6])([#6])[#6]",

    "nitrile": "[CX2]#[NX1]",

    "alkene": "[CX3;!$(C=O)]=[CX3;!$(C=O)]",

    "alkyne": "[CX2]#[CX2]",

    "benzene ring": "[c;!$(c[OX2H])]1[c;!$(c[OX2H])][c;!$(c[OX2H])][c;!$(c[OX2H])][c;!$(c[OX2H])][c;!$(c[OX2H])]1",

    "halide": "[F,Cl,Br,I]",

    "alkyl halide": "[CX4;!$(C=O)][F,Cl,Br,I]",

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

    "sulfonyl chloride": "[#6][SX4](=O)(=O)Cl",

    "sulfonyl fluoride": "[#6][SX4](=O)(=O)F",

    "sulfonyl bromide": "[#6][SX4](=O)(=O)Br",

    "sulfonyl iodide": "[#6][SX4](=O)(=O)I",

    "phosphate ester": "[PX4](=O)([OX2][#6])([OX2,O])([OX2,O])",

    "phosphine": "[PX3;!$(P=O);!$(P=S);!$(P=N)]([#6,#1,#9,#17,#35,#53])",

    "phosphine oxide": "[PX4](=O)([#6,#1])([#6,#1])[#6,#1]",

    "phosphonate": "[PX4](=O)([#6])([OX2,O])([OX2,O])",

    "phosphonium": "[P+X4]",

    "epoxide": "[OX2r3]1[#6r3][#6r3]1",

    "acyl chloride": "[CX3](=O)Cl",

    "anhydride": "[CX3](=O)[OX2][CX3](=O)",

    "lactone": "[CX3r](=O)[OX2r]",

    "lactam": "[CX3r](=O)[NX3r]",
}