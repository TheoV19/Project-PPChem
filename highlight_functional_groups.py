import pubchempy as pcp 
import rdkit as rd
from rdkit import Chem 
from functional_groups import functional_groups, detect_functional_groups
from rdkit.Chem.Draw import rdMolDraw2D
import re

def draw_molecule_with_functional_groups(smiles, filename="highlighted_molecule.svg"):

    """

    Draws a molecule with detected functional groups highlighted.

    Each functional group gets a different color.

    Uses:

        detect_functional_groups(smiles)

        functional_groups dictionary

    """

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:

        raise ValueError("Invalid Molecule inserted.")

    detected_groups = detect_functional_groups(smiles)

    colors = [
    (1.0, 0.6, 0.6),  
    (0.6, 0.9, 0.6),   
    (0.6, 0.7, 1.0),   
    (1.0, 0.8, 0.5),   
    (0.8, 0.6, 1.0),   
    (0.6, 0.9, 0.9),   
    (1.0, 0.7, 0.9),   
    (0.9, 0.9, 0.6),   
]
    highlight_atoms = set()

    highlight_bonds = set()

    atom_colors = {}

    bond_colors = {}

    for index, (group, data) in enumerate(detected_groups.items()):

        pattern = Chem.MolFromSmarts(functional_groups[group])

        color = colors[index % len(colors)]

        for match in data["position"]:

            highlight_atoms.update(match)

            for atom_idx in match:

                atom_colors[atom_idx] = color

            for bond in pattern.GetBonds():

                atom1 = match[bond.GetBeginAtomIdx()]

                atom2 = match[bond.GetEndAtomIdx()]

                mol_bond = mol.GetBondBetweenAtoms(atom1, atom2)

                if mol_bond is not None:

                    bond_idx = mol_bond.GetIdx()

                    highlight_bonds.add(bond_idx)

                    bond_colors[bond_idx] = color

    drawer = rdMolDraw2D.MolDraw2DSVG(600, 600)

    rdMolDraw2D.PrepareAndDrawMolecule(

        drawer,

        mol,

        highlightAtoms=list(highlight_atoms),

        highlightBonds=list(highlight_bonds),

        highlightAtomColors=atom_colors,

        highlightBondColors=bond_colors

    )

    drawer.FinishDrawing()

    svg = drawer.GetDrawingText()

    with open(filename, "w", encoding="utf-8") as file:

        file.write(svg)

    return svg

draw_molecule_with_functional_groups(
    "OC[C@H]1O[C@@H](c2ccc(Cl)c(Cc3ccc(O[C@H]4CCOC4)cc3)c2)[C@H](O)[C@@H](O)[C@@H]1O",
    "penis.svg"
)
