#type:ignore
import pytest
import pandas as pd
from organomind.aromatic import detect_aromatic

def test_detect_aromatic_benzene():
    result = detect_aromatic("c1ccccc1")  
    assert isinstance(result, pd.DataFrame)
    assert result["Aromatic Group"].iloc[0] != "None"

def test_detect_aromatic_not_aromatic():
    result = detect_aromatic("CC(=O)O")  
    assert isinstance(result, pd.DataFrame)
    assert result["Aromatic Group"].iloc[0] == "None"

def test_detect_aromatic_aspirin():
    result = detect_aromatic("CC(=O)Oc1ccccc1C(=O)O")  
    assert isinstance(result, pd.DataFrame)
    assert len(result) > 0

def test_detect_aromatic_invalid_smiles():
    with pytest.raises(ValueError):
        detect_aromatic("invalid_smiles")