#type:ignore
import pytest
from organomind.acidity import acid_base_estimate

def test_acidity_found():
    smiles = "CC(=O)O"
    df_acidic, df_basic = acid_base_estimate(smiles)
    assert df_basic.empty
    assert df_acidic.iloc[0]["group"] == "carboxylic acid"
    assert df_acidic.iloc[0]["type"] == "acidic"
    assert df_acidic.iloc[0]["strength"] == "weak"
    assert df_acidic.iloc[0]["pka_range"] == "4-5"
    assert df_acidic.iloc[0]["priority"] == 2
    assert df_acidic.iloc[0]["count"] == 1

def test_acidity_not_found():
    smiles = "c1ccccc1"
    df_acidic, df_basic = acid_base_estimate(smiles)
    assert df_acidic.empty
    assert df_basic.empty

def test_acidity_invalid_smiles():
    with pytest.raises(ValueError):
        acid_base_estimate("Invalid_smiles")