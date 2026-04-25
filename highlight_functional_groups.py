import pubchempy as pcp 
import rdkit as rd
from rdkit import Chem 
from functional_groups import functional_groups, detect_functional_groups
from rdkit.Chem.Draw import rdMolDraw2D
import re


def rgb_to_svg_color(color):
    """
    Converts RDKit color tuple like (1.0, 0.6, 0.6)
    into SVG color like rgb(255,153,153)
    """
    r, g, b = color
    return f"rgb({int(r * 255)}, {int(g * 255)}, {int(b * 255)})"


def add_legend_to_svg(svg, legend_items, width=800, x=0, y=0):
    """
    Adds a legend to the top-right of an RDKit SVG.

    legend_items will look like: [
        ("carboxylic_acid", (1.0, 0.6, 0.6)),
        ("ester", (0.6, 0.9, 0.6)),
        ...]
    """
    if not legend_items:
        return svg

    line_height = 22
    box_size = 12
    padding = 10

    legend_height = padding * 2 + line_height * len(legend_items)
    legend_width = 190

    legend_svg = []
    
    legend_svg.append(
        f"""
        <rect x="{x - padding}" y="{y - padding}"
              width="{legend_width}" height="{legend_height}"
              fill="white" stroke="black" stroke-width="1"
              opacity="0.85" rx="6" ry="6"/>
        """
    )

    # Legend title
    legend_svg.append(
        f"""
        <text x="{x}" y="{y + 5}"
              font-size="13" font-family="Arial"
              font-weight="bold" fill="black">
              Functional groups
        </text>
        """
    )

    current_y = y + 25

    for group_name, color in legend_items:
        svg_color = rgb_to_svg_color(color)
        clean_name = group_name.replace("_", " ")
        legend_svg.append(
            f"""
            <rect x="{x}" y="{current_y - 10}"
                  width="{box_size}" height="{box_size}"
                  fill="{svg_color}" stroke="black" stroke-width="0.5"/>
            """
        )

        legend_svg.append(
            f"""
            <text x="{x + 20}" y="{current_y}"
                  font-size="12" font-family="Arial"
                  fill="black">
                  {clean_name}
            </text>
            """
        )

        current_y += line_height

    legend_svg = "\n".join(legend_svg)
    svg = svg.replace("</svg>", legend_svg + "\n</svg>")
    return svg

def draw_molecule_with_functional_groups(smiles, filename="highlighted_molecule.svg"):
    """
    Draws a molecule with detected functional groups highlighted.
    Each functional group gets a different color.
    Legend on top right corner.
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

        (0.7, 0.3, 0.6),

        (0.5, 1.0, 0.4),

    ]
    highlight_atoms = set()
    highlight_bonds = set()
    atom_colors = {}
    bond_colors = {}
    legend_items = []

    for index, (group, data) in enumerate(detected_groups.items()):
        pattern = Chem.MolFromSmarts(functional_groups[group])
        color = colors[index]

        legend_items.append((group, color))

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

    drawer = rdMolDraw2D.MolDraw2DSVG(900, 900)

    rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol,
        highlightAtoms=list(highlight_atoms), highlightBonds=list(highlight_bonds), 
        highlightAtomColors=atom_colors, highlightBondColors=bond_colors)

    drawer.FinishDrawing()

    svg = drawer.GetDrawingText()

    svg = add_legend_to_svg(svg, legend_items, width=700, x=700, y=25)

    with open(filename, "w", encoding="utf-8") as file:

        file.write(svg)

    return svg

draw_molecule_with_functional_groups(
    "O=C1[C@@H]2OC3=C(O)C=CC4=C3[C@@]2([C@]5(CC1)O)CCN(CC=C)[C@@H]5C4",
    "momo_leonardo_dicaprio.svg"
)
