#type: ignore
import pytest
from organomind.functional_groups import detect_functional_groups

def test_functional_groups_found():
    smiles = "CC(=O)O"
    result = detect_functional_groups(smiles)
    assert "carboxylic acid" in result
    assert result["carboxylic_acid"]["amount"] == 1

def test_functional_groups_not_found():
    smiles = "O"
    result = detect_functional_groups(smiles)
    assert result == {}

def test_functional_groups_invalid_smiles():
    with pytest.raises(ValueError):
        detect_functional_groups("Invalid_smiles")