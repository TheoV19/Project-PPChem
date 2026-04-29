import pubchempy as pcp 
import rdkit as rd
from rdkit import Chem 
from functional_groups import detect_functional_groups

acid_base_info = {
    "carboxylic_acid": {
        "type": "acidic",
        "strength": "weak",
        "pka_range": "4-5",
        "priority": 2
    },

    "phenol": {
        "type": "acidic",
        "strength": "very weak",
        "pka_range": "9-10",
        "priority": 4
    },

    "alcohol": {
        "type": "acidic",
        "strength": "extremely weak",
        "pka_range": "16-18",
        "priority": 6
    },

    "thiol": {
        "type": "acidic",
        "strength": "weak ",
        "pka_range": "8-11",
        "priority": 4
    },

    "sulfonamide": {
        "type": "acidic",
        "strength": "weak",
        "pka_range": "6-10",
        "priority": 3
    },

    "phosphate_ester": {
        "type": "acidic",
        "strength": "depends on structure",
        "pka_range": "depends on structure",
        "priority": 2
    },

    "primary_amine": {
        "type": "basic",
        "strength": "weak",
        "pka_range": "conjugate acid pKa 9-11",
        "priority": 1
    },

    "secondary_amine": {
        "type": "basic",
        "strength": "moderate",
        "pka_range": "conjugate acid pKa 9-11",
        "priority": 1
    },

    "tertiary_amine": {
        "type": "basic",
        "strength": "strong",
        "pka_range": "conjugate acid pKa 8-11",
        "priority": 1
    },

    "imine": {
        "type": "basic",
        "strength": "weak",
        "pka_range": "conjugate acid pKa 5-7",
        "priority": 3
    },

    "amide": {
        "type": "basic",
        "strength": "very weak",
        "pka_range": "conjugate acid pKa < 1",
        "priority": 5
    }
}

def acid_base_estimate (smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid Molecule inserted.")
    
    detected_groups = detect_functional_groups(smiles)
    acidic_groups=[]
    basic_groups=[]
    
    for group, group_info in detected_groups.items():
        if group not in acid_base_info:
            continue
        values=acid_base_info[group]
        result = {
            "group": group,
            "count": group_info["amount"],
            "positions": group_info["position"],
            "type": values["type"],
            "strength": values["strength"],
            "pka_range": values["pka_range"],
            "priority": values["priority"]
        }
        
        if values["type"]=="acidic":
            acidic_groups.append(result)
        elif values["type"]=="basic":
            basic_groups.append(result)
        
    acidic_groups.sort(key=lambda x: x["priority"])
    basic_groups.sort(key=lambda x: x["priority"])
    
    print (acidic_groups, basic_groups)
    return acidic_groups, basic_groups
