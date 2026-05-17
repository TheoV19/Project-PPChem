#type: ignore
from organomind.highlight_functional_groups import draw_molecule_with_functional_groups
import pytest

def test_draw_molecule_with_functional_groups_none():
    smiles = "O"
    result = draw_molecule_with_functional_groups(smiles)
    assert result is None

def test_draw_molecule_with_functional_groups_is():
    smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    result = draw_molecule_with_functional_groups(smiles)
    assert result is not None

def test_draw_molecule_with_functional_groups_invalid_smiles():
    with pytest.raises(ValueError):
        draw_molecule_with_functional_groups("Invalid_smiles")