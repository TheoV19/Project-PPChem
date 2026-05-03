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
from functions.aromatic import detect_aromaticity
from functions.point_groups import find_group

st.title("OrganoMind")
st.image("image.png", width =500)

st.header("Welcom on OrganoMind, your organic chemistry assistant 🧪 using PubChem database ! ")
st.subheader("You can search informations on any existant molecules by entering its name, formula, smiles, inchi, inchikey:")
search_type = st.selectbox("Enter:", ["name", "formula", "smiles", "inchi", "inchikey"])
urequest = st.text_input(f"Enter the {search_type}")

info = st.multiselect("I want informations about:", options=["Molecular formula", "Molecular weight", "IUPAC name", "SMILES", "CAS", "Number of rotable bond", "Number of stereocenter", "3D drawing"], default=["Molecular formula"])

def filter_cas(synonyms: list[str])-> list[str]:
    cas = []
    for s in synonyms:
        match = re.match("(\d{2,7}-\d\d-\d)", s)
        if match:
            return  match.group(1)
    return None

#User enter name, molecular formula,...
if urequest:
    with st.spinner("Searching PubChem..."):
        results = pcp.get_compounds(urequest, search_type)
        if results:
            c = results[0]
            st.success("Compound found!")
            st.write("**Formula:**", c.molecular_formula)
            st.write("**Molecular Weight:**", c.molecular_weight, "g$\cdot$mol$^{-1}$")
            st.write("**IUPAC Name:**", c.iupac_name)
            st.write("**Smiles**", c.smiles)
            st.write("**CAS**", filter_cas(c.synonyms))
            st.write("**Number of rotable bond:**", c.rotatable_bond_count)

    
            st.write("**Number of chiral center:**", chiral_center(c.smiles))
            st.write("**Number of existant isomers:**", find_isomers(c.smiles))
            st.write("**Representation of chiral center on the molecule's 2D drawing:**")
            color_chiral(c.smiles)


            st.write("**The functional groups present in the molecule are:**")
            st.dataframe(detect_functional_groups(c.smiles))
            #Add the 2D drawing of the molecule with functional group highlighted


            # nb_aromatic = detect_aromaticity(c.smiles)
            # st.write("**Number of aromatic ring:**", nb_aromatic)


            df_acidic, df_basic = acid_base_estimate(c.smiles)
            st.write("**Acidic groups:**")
            st.dataframe(df_acidic)
            st.write("**Basic groups:**")
            st.dataframe(df_basic)


            st.write("**Point group of the molecule:**", find_group(c.smiles))


            st.write("**3D drawing of the molecule**")
            draw_molecule_3d(c.smiles)
        
        else:
            st.error("No compound found.")

#User draw
st.subheader("or by drawing it:")
drawing = st_ketcher()

if drawing:
    with st.spinner("searching PubChem..."):
        result = pcp.get_compounds(drawing, "smiles")
        if result:
            c = result[0]
            st.success("Compound found!")
            st.write("**Formula:**", c.molecular_formula)
            st.write("**Molecular Weight:**", c.molecular_weight, "g$\cdot$mol$^{-1}$")
            st.write("**IUPAC Name:**", c.iupac_name)
            st.write("**Smiles**", c.smiles)
            #st.write("**Common names:**")
            #for s in c.synonyms[:5]:
               # st.write("•", s)
            st.write("**CAS**", filter_cas(c.synonyms))
            st.write("**Number of rotable bond:**", c.rotatable_bond_count)
            st.write("**Number of stereocenter**", c.defined_atom_stereo_count)
        else:
            st.error("No compound found.") 




