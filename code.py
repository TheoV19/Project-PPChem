# type: ignore
import pubchempy as pcp  # type: ignore
from rdkit import Chem
from rdkit.Chem import Draw
import streamlit as st
from streamlit_ketcher import st_ketcher
import re
from organomind.draw3D import draw_molecule_3d
from organomind.functional_groups import detect_functional_groups
import pandas as pd
from organomind.stereo import chiral_center, color_chiral, find_isomers
from organomind.acidity import acid_base_estimate
from organomind.aromatic import detect_aromatic
from organomind.point_groups import find_group
from organomind.nucelo_electro import electro_nucleo_sites_hsab
from organomind.highlight_functional_groups import draw_molecule_with_functional_groups


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





# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
# st.set_page_config(
#     page_title="OrganoMind",
#     page_icon="🧪",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ── GLOBAL CSS ───────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
#     /* Font & background */
#     @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
#     html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
#     .main { background-color: #0f1117; }

#     /* Hide default Streamlit header */
#     #MainMenu, footer, header { visibility: hidden; }

#     /* ── NAVBAR ── */
#     .navbar {
#         background: linear-gradient(90deg, #1a1f2e, #2d3561);
#         padding: 1rem 2rem;
#         border-radius: 12px;
#         display: flex;
#         align-items: center;
#         justify-content: space-between;
#         margin-bottom: 2rem;
#         box-shadow: 0 4px 20px rgba(0,0,0,0.4);
#     }
#     .navbar-title {
#         font-size: 1.8rem;
#         font-weight: 700;
#         color: #7dd3fc;
#         letter-spacing: 1px;
#     }
#     .navbar-subtitle {
#         font-size: 0.85rem;
#         color: #94a3b8;
#     }

#     /* ── CARDS ── */
#     .card {
#         background: #1e2333;
#         border: 1px solid #2d3561;
#         border-radius: 12px;
#         padding: 1.5rem;
#         margin-bottom: 1.5rem;
#         box-shadow: 0 2px 12px rgba(0,0,0,0.3);
#     }
#     .card-title {
#         font-size: 1rem;
#         font-weight: 600;
#         color: #7dd3fc;
#         margin-bottom: 1rem;
#         padding-bottom: 0.5rem;
#         border-bottom: 1px solid #2d3561;
#     }

#     /* ── RESULT BADGE ── */
#     .result-badge {
#         background: #0f2942;
#         border-left: 4px solid #7dd3fc;
#         border-radius: 0 8px 8px 0;
#         padding: 0.6rem 1rem;
#         margin: 0.4rem 0;
#         font-size: 0.95rem;
#         color: #e2e8f0;
#     }
#     .result-label {
#         color: #7dd3fc;
#         font-weight: 600;
#         margin-right: 0.5rem;
#     }

#     /* ── SECTION HEADER ── */
#     .section-header {
#         font-size: 1.1rem;
#         font-weight: 600;
#         color: #e2e8f0;
#         margin: 1.5rem 0 0.8rem 0;
#         display: flex;
#         align-items: center;
#         gap: 0.5rem;
#     }
#     .section-divider {
#         height: 1px;
#         background: linear-gradient(90deg, #2d3561, transparent);
#         margin: 1rem 0;
#     }

#     /* ── BUTTONS ── */
#     .stButton > button {
#         background: linear-gradient(135deg, #2d3561, #3d4f8f);
#         color: #e2e8f0;
#         border: 1px solid #4a5fa0;
#         border-radius: 8px;
#         padding: 0.5rem 1.5rem;
#         font-weight: 600;
#         transition: all 0.2s;
#         width: 100%;
#     }
#     .stButton > button:hover {
#         background: linear-gradient(135deg, #3d4f8f, #5068b5);
#         border-color: #7dd3fc;
#         color: #7dd3fc;
#     }

#     /* ── INPUTS ── */
#     .stTextInput > div > div > input,
#     .stSelectbox > div > div {
#         background: #1e2333 !important;
#         border: 1px solid #2d3561 !important;
#         border-radius: 8px !important;
#         color: #e2e8f0 !important;
#     }

#     /* ── SIDEBAR ── */
#     [data-testid="stSidebar"] {
#         background: #1a1f2e;
#         border-right: 1px solid #2d3561;
#     }
#     [data-testid="stSidebar"] .stMarkdown { color: #94a3b8; }

#     /* ── SUCCESS / ERROR ── */
#     .stSuccess { border-radius: 8px !important; }
#     .stAlert { border-radius: 8px !important; }

#     /* ── DATAFRAME ── */
#     .dataframe { border-radius: 8px !important; }

#     /* ── TABS ── */
#     .stTabs [data-baseweb="tab-list"] {
#         background: #1e2333;
#         border-radius: 10px;
#         padding: 4px;
#     }
#     .stTabs [data-baseweb="tab"] {
#         border-radius: 8px;
#         color: #94a3b8;
#     }
#     .stTabs [aria-selected="true"] {
#         background: #2d3561 !important;
#         color: #7dd3fc !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ── NAVBAR ───────────────────────────────────────────────────────────────────
# st.markdown("""
# <div class="navbar">
#     <div>
#         <div class="navbar-title">🧪 OrganoMind</div>
#         <div class="navbar-subtitle">Organic Chemistry Assistant · Powered by PubChem & RDKit</div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # ── SIDEBAR ───────────────────────────────────────────────────────────────────
# with st.sidebar:
#     st.markdown("### ⚙️ Analysis options")
#     st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)

#     info = st.multiselect(
#         "Select the information to display:",
#         options=[
#             "Molecular formula",
#             "Molecular weight",
#             "IUPAC name",
#             "SMILES",
#             "CAS",
#             "Number of rotable bond",
#             "Stereochemistry",
#             "Functional group",
#             "Aromaticity",
#             "Acidity/Basicity",
#             "Nucleophilicity/Electrophilicity",
#             "Point groups",
#             "3D drawing"
#         ],
#         default=["Molecular formula", "Molecular weight", "IUPAC name"]
#     )

#     st.markdown("<div class='section-divider'></div>", unsafe_allow_html=True)
#     st.markdown("""
#     <div style='color:#94a3b8; font-size:0.8rem;'>
#     💡 <b>Tips</b><br>
#     • Use SMILES for precise structures<br>
#     • CAS numbers are highly reliable<br>
#     • 3D drawing may take a few seconds
#     </div>
#     """, unsafe_allow_html=True)

# # ── HELPER FUNCTIONS ─────────────────────────────────────────────────────────
# def filter_cas(synonyms: list[str]) -> str | None:
#     for s in synonyms:
#         match = re.match(r"(\d{2,7}-\d\d-\d)", s)
#         if match:
#             return match.group(1)
#     return None

# def result_row(label, value):
#     st.markdown(f"""
#     <div class='result-badge'>
#         <span class='result-label'>{label}</span>{value}
#     </div>
#     """, unsafe_allow_html=True)

# def display_results(c):
#     """Display all selected info for a compound."""

#     # Basic info block
#     basic = any(x in info for x in ["Molecular formula", "Molecular weight", "IUPAC name", "SMILES", "CAS", "Number of rotable bond"])
#     if basic:
#         st.markdown("<div class='card'><div class='card-title'>📋 General Information</div>", unsafe_allow_html=True)
#         if "Molecular formula" in info:
#             result_row("Formula:", c.molecular_formula)
#         if "Molecular weight" in info:
#             result_row("Molecular Weight:", f"{c.molecular_weight} g/mol")
#         if "IUPAC name" in info:
#             result_row("IUPAC Name:", c.iupac_name)
#         if "SMILES" in info:
#             result_row("SMILES:", f"<code>{c.smiles}</code>")
#         if "CAS" in info:
#             result_row("CAS:", filter_cas(c.synonyms) or "N/A")
#         if "Number of rotable bond" in info:
#             result_row("Rotatable Bonds:", c.rotatable_bond_count)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Stereochemistry
#     if "Stereochemistry" in info:
#         st.markdown("<div class='card'><div class='card-title'>🔄 Stereochemistry</div>", unsafe_allow_html=True)
#         col1, col2 = st.columns(2)
#         with col1:
#             result_row("Chiral centers:", chiral_center(c.smiles))
#         with col2:
#             result_row("Possible isomers:", find_isomers(c.smiles))
#         color_chiral(c.smiles)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Functional groups
#     if "Functional group" in info:
#         st.markdown("<div class='card'><div class='card-title'>🔬 Functional Groups</div>", unsafe_allow_html=True)
#         st.dataframe(detect_functional_groups(c.smiles), use_container_width=True)
#         draw_molecule_with_functional_groups(c.smiles)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Aromaticity
#     if "Aromaticity" in info:
#         st.markdown("<div class='card'><div class='card-title'>⭕ Aromaticity</div>", unsafe_allow_html=True)
#         st.dataframe(detect_aromatic(c.smiles), use_container_width=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Acidity/Basicity
#     if "Acidity/Basicity" in info:
#         st.markdown("<div class='card'><div class='card-title'>⚗️ Acidity / Basicity</div>", unsafe_allow_html=True)
#         df_acidic, df_basic = acid_base_estimate(c.smiles)
#         col1, col2 = st.columns(2)
#         with col1:
#             st.markdown("**🔴 Acidic groups**")
#             st.dataframe(df_acidic, use_container_width=True)
#         with col2:
#             st.markdown("**🔵 Basic groups**")
#             st.dataframe(df_basic, use_container_width=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Nucleophilicity/Electrophilicity
#     if "Nucleophilicity/Electrophilicity" in info:
#         st.markdown("<div class='card'><div class='card-title'>⚡ Nucleophilicity / Electrophilicity</div>", unsafe_allow_html=True)
#         st.dataframe(electro_nucleo_sites_hsab(c.smiles), use_container_width=True)
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Point groups
#     if "Point groups" in info:
#         st.markdown("<div class='card'><div class='card-title'>🔷 Symmetry</div>", unsafe_allow_html=True)
#         result_row("Point Group:", find_group(c.smiles))
#         st.markdown("</div>", unsafe_allow_html=True)

#     # 3D drawing
#     if "3D drawing" in info:
#         st.markdown("<div class='card'><div class='card-title'>🧬 3D Structure</div>", unsafe_allow_html=True)
#         draw_molecule_3d(c.smiles)
#         st.markdown("</div>", unsafe_allow_html=True)

# # ── MAIN TABS ─────────────────────────────────────────────────────────────────
# tab1, tab2 = st.tabs(["🔍 Search by name / formula", "✏️ Draw a molecule"])

# # ── TAB 1 : SEARCH ────────────────────────────────────────────────────────────
# with tab1:
#     st.markdown("<div class='card'><div class='card-title'>🔍 Molecule Search</div>", unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 3])
#     with col1:
#         search_type = st.selectbox("Search by:", ["name", "formula", "smiles", "inchi", "inchikey"])
#     with col2:
#         urequest = st.text_input(f"Enter the {search_type}", placeholder=f"e.g. aspirin, C9H8O4, CC(=O)Oc1ccccc1C(=O)O...")
#     st.markdown("</div>", unsafe_allow_html=True)

#     if urequest:
#         with st.spinner("🔎 Searching PubChem database..."):
#             results = pcp.get_compounds(urequest, search_type)
#             if results:
#                 c = results[0]
#                 st.success(f"✅ Compound found: **{c.iupac_name or urequest}**")
#                 display_results(c)
#             else:
#                 st.error("❌ No compound found. Check the spelling or try a different search type.")

# # ── TAB 2 : DRAW ──────────────────────────────────────────────────────────────
# with tab2:
#     st.markdown("<div class='card'><div class='card-title'>✏️ Draw your molecule</div>", unsafe_allow_html=True)
#     st.markdown("<p style='color:#94a3b8; font-size:0.9rem;'>Use the editor below to draw any molecule. The SMILES will be generated automatically.</p>", unsafe_allow_html=True)
#     drawing = st_ketcher()
#     st.markdown("</div>", unsafe_allow_html=True)

#     if drawing:
#         with st.spinner("🔎 Identifying molecule..."):
#             result = pcp.get_compounds(drawing, "smiles")
#             if result:
#                 c = result[0]
#                 st.success(f"✅ Compound identified: **{c.iupac_name or 'Unknown'}**")
#                 display_results(c)
#             else:
#                 st.error("❌ Molecule not found in PubChem. Try a known compound.")


# st.set_page_config("OrganoMind 🧪", layout="wide")

# st.title("🧪 OrganoMind")
# st.caption("Organic Chemistry Assistant · PubChem + RDKit")

# info = st.sidebar.multiselect(
#     "Select information to display",
#     [
#         "Formula", "Molecular weight", "IUPAC name",
#         "SMILES", "CAS", "Rotatable bonds",
#         "Stereochemistry", "Functional groups",
#         "Aromaticity", "Acidity/Basicity",
#         "3D structure"
#     ],
#     default=["Formula", "Molecular weight", "IUPAC name"]
# )



# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="OrganoMind",
    page_icon="🧪",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("🧪 OrganoMind")
st.caption("Organic Chemistry Assistant · PubChem + RDKit")
st.caption("EPFL · 2nd Year · Practical Programming in Chemistry · 2026")

st.markdown("---")

# =========================
# INTRODUCTION
# =========================
st.markdown("""
**OrganoMind** is an organic chemistry assistant that enables **3D visualization of molecules**
with built-in features providing chemical and stereochemical properties — helping you better
understand reactivity and chemical processes. Enter a molecule by name, formula, SMILES or
draw it directly, and OrganoMind gives you everything you need.
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🧬 3D Visualization")
    st.markdown("🔄 Stereochemistry")
    st.markdown("🔷 Point Groups")
with col2:
    st.markdown("🔬 Functional Groups")
    st.markdown("⚗️ Acidity / Basicity")
    st.markdown("🏷️ IUPAC Naming")
with col3:
    st.markdown("⭕ Aromaticity")
    st.markdown("⚡ Nucleophilicity")
    st.markdown("🔑 CAS / SMILES")

st.markdown("---")
st.markdown("👥 **Team:** Theo Vienne · Noam Balter-Dejeux · Tolga Seckin · Theo Morales Crassier")
st.markdown("---")

# =========================
# SIDEBAR OPTIONS
# =========================
st.sidebar.header("⚙️ Analysis Options")

info = st.sidebar.multiselect(
    "Select information to display:",
    [
        "Molecular formula",
        "Molecular weight",
        "IUPAC name",
        "SMILES",
        "CAS",
        "Rotatable bonds",
        "Stereochemistry",
        "Functional groups",
        "Aromaticity",
        "Acidity/Basicity",
        "Nucleophilicity/Electrophilicity",
        "Point groups",
        "3D drawing"
    ],
    default=["Molecular formula", "Molecular weight", "IUPAC name"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: SMILES gives most accurate structure results")

# =========================
# HELPERS
# =========================
def filter_cas(synonyms: list[str]):
    if synonyms is None:
        return None
    for s in synonyms:
        match = re.match(r"(\d{2,7}-\d\d-\d)", s)
        if match:
            return match.group(1)
    return None

def show(label, value):
    st.write(f"**{label}** {value}")

# =========================
# RESULT DISPLAY
# =========================
def display_results(c):

    st.subheader("📋 General Information")

    if "Molecular formula" in info:
        show("Formula:", c.molecular_formula)
        
    if "Molecular weight" in info:
        show("Weight:", f"{c.molecular_weight} g/mol")

    if "IUPAC name" in info:
        show("IUPAC:", c.iupac_name)

    if "SMILES" in info:
        st.code(c.smiles)

    if "CAS" in info:
        show("CAS:", filter_cas(c.synonyms) or "N/A")

    if "Rotatable bonds" in info:
        show("Rotatable bonds:", c.rotatable_bond_count)



    if "Stereochemistry" in info:
        st.subheader("🔄 Stereochemistry")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Chiral centers:", chiral_center(c.smiles))
        with col2:
            st.write("Possible isomers:", find_isomers(c.smiles))
        
        img = color_chiral(c.smiles)
        if img is None:
            st.info("No chiral centers found.")
        else:
            st.image(img, caption="Highlighted chiral centers")



    if "Functional groups" in info:
        st.subheader("🔬 Functional Groups")
        st.dataframe(detect_functional_groups(c.smiles))
        draw_molecule_with_functional_groups(c.smiles)

    if "Aromaticity" in info:
        st.subheader("⭕ Aromaticity")
        st.dataframe(detect_aromatic(c.smiles))

    if "Acidity/Basicity" in info:
        st.subheader("⚗️ Acidity / Basicity")
        acidic, basic = acid_base_estimate(c.smiles)
        col1, col2 = st.columns(2)
        with col1:
            st.write("🔴 Acidic sites")
            st.dataframe(acidic)
        with col2:
            st.write("🔵 Basic sites")
            st.dataframe(basic)

    if "Nucleophilicity/Electrophilicity" in info:
        st.subheader("⚡ Reactivity")
        st.dataframe(electro_nucleo_sites_hsab(c.smiles))

    if "Point groups" in info:
        st.subheader("🔷 Symmetry")
        st.write("Point group:", find_group(c.smiles))

    if "3D drawing" in info:
        st.subheader("🧬 3D Structure")
        draw_molecule_3d(c.smiles)

# =========================
# TABS
# =========================
tab1, tab2 = st.tabs(["🔍 Search", "✏️ Draw"])

# =========================
# TAB 1 - SEARCH
# =========================
with tab1:
    st.subheader("Molecule Search")
    col1, col2 = st.columns([1, 2])
    with col1:
        search_type = st.selectbox(
            "Search by:",
            ["name", "formula", "smiles", "inchi", "inchikey"]
        )
    with col2:
        query = st.text_input("Enter molecule")

    if query:
        with st.spinner("Searching PubChem..."):
            results = pcp.get_compounds(query, search_type)
            if results:
                compound = results[0]
                st.success(f"Found: {compound.iupac_name or query}")
                display_results(compound)
            else:
                st.error("No compound found")

# =========================
# TAB 2 - DRAW
# =========================
with tab2:
    st.subheader("Draw Molecule")
    st.info("Draw a molecule to analyze its structure")
    drawing = st_ketcher()

    if drawing:
        with st.spinner("Processing molecule..."):
            result = pcp.get_compounds(drawing, "smiles")
            if result:
                compound = result[0]
                st.success(f"Identified: {compound.iupac_name or 'Unknown'}")
                display_results(compound)
            else:
                st.error("Molecule not found in PubChem")