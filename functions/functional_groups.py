import pubchempy as pcp # type: ignore
import rdkit as rd
from rdkit import Chem 
import pandas as pd #type: ignore

def detect_functional_groups(smiles, return_df = True):
    """
    Finds functional groups if present.
    Args:
        smiles (str): SMILES string of the molecule.
    Returns:
        dict: A dictionay of detected functional groups and the amount of times.
    """
    mol = Chem.MolFromSmiles(smiles)
   
    groups_present={}
    
    if mol is None:
        raise ValueError("Invalid Molecule inserted.")

    for group, smart in functional_groups.items():
        pattern=Chem.MolFromSmarts(smart)
        matches=mol.GetSubstructMatches(pattern)
        
        if len (matches)>0:
            groups_present[group]={
                "amount": len(matches),
                "position": matches
            }
    df = pd.DataFrame([{"Functional Group": group, "Count": data["amount"], "Position": data["position"]} for group, data in groups_present.items()])

    if return_df:
        return df

    return groups_present