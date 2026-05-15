# -            OrganoMind           -


## 📚General informations📚
OrganoMind is a project developped as part of Practical Progamming in chemistry EPFL (2026) during second year of study. OrganoMind is thought as a organic chemistry assistant that allows 3D visualization of molecules with built-in features that give both chemical and stereochemical properties that allows better understanding of chemical processes. 

### 💪Features💪 
- 3D visualization of molecules and IUPAC naming.
- Detection and 2D visualization of functionnal groups. 
- Detection of aromatic groups and nomenclature of the group.
- Detection of chiral centers, number of isomers and 2D visualization of the chiral center. 
- Detection of acidic and basic groups, and estimation of the pKa of the molecule.
- Detection of nucleophilic and electrophilic groups with attribution of the nucleophilic/electrophilic level.
- Determination of molecule's point group.

### 👥Contributions👥
Théo Vienne
[![GitHub](https://img.shields.io/badge/GitHub-TheoV19-181717?logo=github)](https://github.com/TheoV19)  

Noam Balter-Dejeux
[![GitHub](https://img.shields.io/badge/GitHub-NoamBalter-181717?logo=github)](https://github.com/NoamBalter)  

Tolga Seckin
[![GitHub](https://img.shields.io/badge/GitHub-tolgaseckin-181717?logo=github)](https://github.com/tolgaseckin)  

Théo Morales Crassier
[![GitHub](https://img.shields.io/badge/GitHub-theo--moralescrassier-181717?logo=github)](https://github.com/theo-moralescrassier)  


### 📈A useful assistant📈
Organomind is thought as a tool to simplify the understanding of the reactivity of complex chemical compounds. By either putting directly the structure or the name or the formula or even the smile of a molecule, organomind will give you all the characteritcis you need to work on your problem.

#### You need compute a reaction path for a synthesis ? 
Put your reactants in organomind and it will tell you which group of your molecule are nucleophilic and electrophilic with all functional groups, allowing you to determine accuratly which part will react and with what.

#### Struggle with a MO diagram ? 
Organomind will give you the point group allowing to simplify your work and focus on the important part of your search.

#### Working on a stereospcific synthesis ?
Organomind will give you the number of chiral centers and 2D view of them with the number of stable isomers which then allow you properly classify the stereo-isomers of your molecule.

Already convinced ? Let us show you how to install it and enjoy all the features of this framework ! 🎉

## ⚙️ Installation ⚙️

### Prerequisites
- Python 3.10 or higher
- pip

### Steps

**1. Create a CONDA virtual environment (recommended)**
```bash
#Open bash or terminal
#Name the environment as you wish and specify python 3.10
conda create -n env.name python=3.10

#Activate your environment
conda activate env.name
```

**2. Two ways to proceed**

*A. Using the repo:*
```bash
#Clone the repository
git clone https://github.com/TheoV19/OrganoMind.git

#Naviguate to the Organomind folder
cd path/to/organomind

#Installs the dependencies locally in editable mode, make sure to activate your environment before doing so
pip install . #installs the dependencies
```

*B. Only using the package:*
```bash
pip install organomind 
    or
pip install git+https://github.com/TheoV19/OrganoMind.git
```


**3. Run the app**
```bash
#In your terminal, you can now run the program with:
organomind-ui
```

The app will open automatically in your browser at `http://localhost:8501`.


 

 
### 🧠How to use🧠
 
#### ✍️Write your molecule anyway you want✍️
OrganoMind supports multiple input formats. In the **Search** tab, select your search type and enter your query:
 
| Input type | Example |
|------------|---------|
| Name | `aspirin` |
| Formula | `C9H8O4` |
| SMILES | `CC(=O)Oc1ccccc1C(=O)O` |
| InChI | `InChI=1S/C9H8O4/...` |
| InChIKey | `BSYNRYMUTXBXSQ-UHFFFAOYSA-N` |
 
> **Tip:** SMILES input gives the most accurate structure results.
 

 
#### 🎨Draw a molecule🎨
 
Switch to the **Draw** tab to use the built-in Ketcher molecular editor. Draw your molecule directly on the canvas and OrganoMind will automatically identify and analyze it.
 

 
### 4. Select the information to display
 
Use the **sidebar** on the left to select which properties you want to compute:
 
- **Molecular formula / weight / IUPAC name / SMILES / CAS** — General information
- **Rotatable bonds** — Conformational flexibility
- **Stereochemistry** — Chiral centers, number of stable isomers, 2D view
- **Functional groups** — Detection and 2D visualization
- **Aromaticity** — Aromatic ring detection and nomenclature
- **Acidity / Basicity** — Acidic and basic site detection with pKa estimation
- **Nucleophilicity / Electrophilicity** — Reactive site detection with HSAB-based level attribution
- **Point groups** — Symmetry group determination
- **3D drawing** — Interactive 3D visualization
 
 













