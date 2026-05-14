#type:ignore
import pytest
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

def test_chiral_center_invalid_smile():
    with pytest.raises(ValueError):
        color_chiral("invalid_smiles")




def test_find_isomers_one():
    smiles = "O"
    assert find_isomers(smiles) == 1


def test_find_isomers_multiple():
    smiles = "OC(F)(Cl)C(F)(Cl)O"
    assert find_isomers(smiles) == 3

def test_find_isomers_multiple():
    with pytest.raises(ValueError):
        color_chiral("invalid_smiles")




def test_color_chiral_none():
    smiles = "CCCC"
    assert color_chiral(smiles) is None


def test_color_chiral_with_chiral():
    smiles = "CCC(C)O"
    result = color_chiral(smiles)
    assert result is not None


def test_color_chiral_no_chiral():
    result = color_chiral("c1ccccc1")  
    assert result is None  

def test_color_chiral_invalid_smiles():
    with pytest.raises(ValueError):
        color_chiral("invalid_smiles")