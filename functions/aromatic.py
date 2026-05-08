import rdkit as rd
from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from functions.Data.aromatic_data import aromatic_patterns
from functions.functional_groups import detect_functional_groups # type: ignore
import pandas as pd #type: ignore

def detect_aromatic(smiles: str) -> pd.DataFrame:
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError("Invalid SMILES string.")

    results = []
    for name, pattern in aromatic_patterns.items():
        if pattern:
            matches = molecule.GetSubstructMatches(pattern)
            if matches:
                results.append({'Aromatic Group': name, 'Count': len(matches), 'Position': [list(m) for m in matches]})

    if not results:
        return pd.DataFrame([{'Aromatic Group': 'None', 'Count': 0, 'Position': []}])

    return pd.DataFrame(results)
         
