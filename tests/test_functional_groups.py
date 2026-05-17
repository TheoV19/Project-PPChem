#type: ignore
import pytest
from organomind.functional_groups import detect_functional_groups, detect_functional_groups_df

def test_functional_groups_found():
    smiles = "CC(=O)O"
    result = detect_functional_groups(smiles)
    assert "carboxylic acid" in result
    assert result["carboxylic acid"]["amount"] == 1

def test_functional_groups_multiple_found():
    smiles = "CC(=O)Oc1ccccc1C(=O)O"
    result = detect_functional_groups(smiles)
    assert "carboxylic acid" in result
    assert "ester" in result
    assert result["carboxylic acid"]["amount"] == 1
    assert result["ester"]["amount"] == 1   

def test_functional_groups_not_found():
    smiles = "O"
    result = detect_functional_groups(smiles)
    assert result == {}

def test_functional_groups_invalid_smiles():
    with pytest.raises(ValueError):
        detect_functional_groups("Invalid_smiles")

def test_functional_groups_df_found():
    smiles = "CC(=O)O"
    result = detect_functional_groups_df(smiles)
    assert result.iloc[0]["Functional Group"] == "carboxylic acid"
    assert result.iloc[0]["Count"] == 1

def test_functional_groups_df_not_found():
    smiles = "O"
    result = detect_functional_groups_df(smiles)
    assert result.empty