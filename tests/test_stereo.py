#type:ignore
from organomind.stereo import chiral_center, find_isomers, color_chiral

def test_chiral_center_is():
    smiles = "CCC(C)O"
    assert chiral_center(smiles) == 1

def test_chiral_center_none():
    smiles = "c1ccccc1"  # benzene → no chiral center
    assert chiral_center(smiles) == 0

def test_chiral_center_multiple():
    smiles = "OC(F)(Cl)C(F)(Cl)O" # 2 chiral centers
    assert chiral_center(smiles) == 2


def test_find_isomers_one():
    smiles = "O"
    assert find_isomers(smiles) == 1


def test_find_isomers_multiple():
    smiles = "OC(F)(Cl)C(F)(Cl)O"
    assert find_isomers(smiles) == 3

def test_color_chiral_none():
    smiles = "CCCC"
    assert color_chiral(smiles) is None