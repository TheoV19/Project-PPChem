#type: ignore
import pytest
from organomind.draw3D import draw_molecule_3d

def test_draw_molecule_3d_valid():
    smiles = "CC(=O)OC1=CC=CC=C1C(=O)O"
    result = draw_molecule_3d(smiles)
    assert result is None


def test_draw_molecule_3d_invalid():
    with pytest.raises(ValueError):
        draw_molecule_3d("invalid_smiles")

