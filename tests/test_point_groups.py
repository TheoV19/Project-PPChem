#type:ignore
import pytest
from organomind.point_groups import find_group

def test_find_group_found():
    smiles = "C(F)(F)(F)F"
    result = find_group(smiles)
    assert "Td" in result

def test_find_group_not_found():
    smiles = "CC(O)C(Cl)Br"
    result = find_group(smiles)
    assert "C1" in result

def test_find_group_invalid_smiles():
    with pytest.raises(ValueError):
        find_group("Invalid_smiles")