# type: ignore
import pubchempy as pcp  # type: ignore
from rdkit import Chem
from rdkit.Chem import Draw
import streamlit as st
from streamlit_ketcher import st_ketcher
import re
from functions.draw3D import draw_molecule_3d
from functions.functional_groups import functional_groups, detect_functional_groups
import pandas as pd
from functions.stereo import chiral_center, color_chiral, find_isomers
from functions.acidity import acid_base_info, acid_base_estimate
from functions.aromatic import aromatic_patterns, detect_aromatic
from functions.point_groups import find_group
from functions.nucelo_electro import HSAB_rules, electro_nucleo_sites_hsab
from functions.highlight_functional_groups import rgb_to_svg_color, add_legend_to_svg, draw_molecule_with_functional_groups

# st.title("OrganoMind")
# st.image("image.png", width =500)

# st.header("Welcom on OrganoMind, your organic chemistry assistant 🧪 using PubChem database ! ")
# st.subheader("You can search informations on any existant molecules by entering its name, formula, smiles, inchi, inchikey:")
# search_type = st.selectbox("Enter:", ["name", "formula", "smiles", "inchi", "inchikey"])
# urequest = st.text_input(f"Enter the {search_type}")

# info = st.multiselect("I want informations about:", 
#                       options=[
#                             "Molecular formula", 
#                             "Molecular weight", 
#                             "IUPAC name", 
#                             "SMILES", 
#                             "CAS", 
#                             "Number of rotable bond", 
#                             "Stereochemistry", "Functional group",
#                             "Aromaticity", "Acidity/Basicity", 
#                             "Nucleophilicity/Electrophilicity", 
#                             "Point groups", "3D drawing"], default=["Molecular formula"])

# def filter_cas(synonyms: list[str])-> list[str]:
#     cas = []
#     for s in synonyms:
#         match = re.match("(\d{2,7}-\d\d-\d)", s)
#         if match:
#             return  match.group(1)
#     return None

# #User enter name, molecular formula,...
# if urequest:
#     with st.spinner("Searching PubChem..."):
#         results = pcp.get_compounds(urequest, search_type)
#         if results:
#             c = results[0]
#             st.success("Compound found!")

#             if "Molecular formula" in info:
#                 st.write("**Formula:**", c.molecular_formula)

#             if "Molecular weight" in info:
#                 st.write("**Molecular Weight:**", c.molecular_weight)

#             if "IUPAC name" in info:
#                 st.write("**IUPAC Name:**", c.iupac_name)

#             if "SMILES" in info:
#                 st.write("**SMILES:**", c.smiles)

#             if "CAS" in info:
#                 st.write("**CAS:**", filter_cas(c.synonyms))

#             if "Number of rotable bond" in info:
#                 st.write("**Rotatable bonds:**", c.rotatable_bond_count)

#             if "Stereochemistry" in info:
#                 st.write("**Number of chiral center:**", chiral_center(c.smiles))
#                 st.write("**Number of existant isomers:**", find_isomers(c.smiles))
#                 color_chiral(c.smiles)

#             if "Functional group" in info:
#                 st.dataframe(detect_functional_groups(c.smiles))
#                 draw_molecule_with_functional_groups(c.smiles)

#             if "Aromaticity" in info:
#                 st.dataframe(detect_aromatic(c.smiles))

#             if "Acidity/Basicity" in info:
#                 df_acidic, df_basic = acid_base_estimate(c.smiles)
#                 st.write("**Acidic groups:**")
#                 st.dataframe(df_acidic)
#                 st.write("**Basic groups:**")
#                 st.dataframe(df_basic)

#             if "Nucleophilicity/Electrophilicity" in info:
#                 st.dataframe(electro_nucleo_sites_hsab(c.smiles))

#             if "Point groups" in info:
#                 st.write("**Point group:**", find_group(c.smiles))

#             if "3D drawing" in info:
#                 draw_molecule_3d(c.smiles)
        
#         else:
#             st.error("No compound found.")

# #User draw
# st.subheader("or by drawing it:")
# drawing = st_ketcher()

# if drawing:
#     with st.spinner("searching PubChem..."):
#         result = pcp.get_compounds(drawing, "smiles")
#         if result:
#             c = result[0]
#             st.success("Compound found!")
#             if "Molecular formula" in info:
#                 st.write("**Formula:**", c.molecular_formula)

#             if "Molecular weight" in info:
#                 st.write("**Molecular Weight:**", c.molecular_weight)

#             if "IUPAC name" in info:
#                 st.write("**IUPAC Name:**", c.iupac_name)

#             if "SMILES" in info:
#                 st.write("**SMILES:**", c.smiles)

#             if "CAS" in info:
#                 st.write("**CAS:**", filter_cas(c.synonyms))

#             if "Number of rotable bond" in info:
#                 st.write("**Rotatable bonds:**", c.rotatable_bond_count)

#             if "Stereochemistry" in info:
#                 st.write("**Number of chiral center:**", chiral_center(c.smiles))
#                 st.write("**Number of existant isomers:**", find_isomers(c.smiles))
#                 color_chiral(c.smiles)

#             if "Functional group" in info:
#                 st.dataframe(detect_functional_groups(c.smiles))
#                 draw_molecule_with_functional_groups(c.smiles)

#             if "Aromaticity" in info:
#                 st.dataframe(detect_aromatic(c.smiles))

#             if "Acidity/Basicity" in info:
#                 df_acidic, df_basic = acid_base_estimate(c.smiles)
#                 st.write("**Acidic groups:**")
#                 st.dataframe(df_acidic)
#                 st.write("**Basic groups:**")
#                 st.dataframe(df_basic)

#             if "Nucleophilicity/Electrophilicity" in info:
#                 st.dataframe(electro_nucleo_sites_hsab(c.smiles))

#             if "Point groups" in info:
#                 st.write("**Point group:**", find_group(c.smiles))

#             if "3D drawing" in info:
#                 draw_molecule_3d(c.smiles)
        
#         else:
#             st.error("No compound found.")




