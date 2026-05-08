from rdkit import Chem

aromatic_patterns = {
    # 6-membered
    'benzene':      Chem.MolFromSmarts('c1ccccc1'),
    'pyridine':     Chem.MolFromSmarts('c1ccncc1'),
    'pyrimidine':   Chem.MolFromSmarts('c1cncnc1'),
    'pyrazine':     Chem.MolFromSmarts('c1cnccn1'),
    'pyridazine':   Chem.MolFromSmarts('c1ccnnc1'),
    'triazine':     Chem.MolFromSmarts('c1ncncn1'),

    # 5-membered
    'furan':        Chem.MolFromSmarts('c1ccoc1'),
    'thiophene':    Chem.MolFromSmarts('c1ccsc1'),
    'pyrrole':      Chem.MolFromSmarts('c1cc[nH]c1'),
    'imidazole':    Chem.MolFromSmarts('c1cn[nH]c1'),
    'pyrazole':     Chem.MolFromSmarts('c1cc[nH]n1'),
    'oxazole':      Chem.MolFromSmarts('c1cnoc1'),
    'thiazole':     Chem.MolFromSmarts('c1cnsc1'),
    'isoxazole':    Chem.MolFromSmarts('c1ccon1'),
    'isothiazole':  Chem.MolFromSmarts('c1ccsn1'),
    'triazole':     Chem.MolFromSmarts('c1cn[nH]n1'),
    'tetrazole':    Chem.MolFromSmarts('c1nn[nH]n1'),

    # Fused bicyclic
    'naphthalene':  Chem.MolFromSmarts('c1ccc2ccccc2c1'),
    'indole':       Chem.MolFromSmarts('c1ccc2[nH]ccc2c1'),
    'benzimidazole':Chem.MolFromSmarts('c1ccc2[nH]cnc2c1'),
    'benzofuran':   Chem.MolFromSmarts('c1ccc2occc2c1'),
    'benzothiophene':Chem.MolFromSmarts('c1ccc2sccc2c1'),
    'quinoline':    Chem.MolFromSmarts('c1ccc2ncccc2c1'),
    'isoquinoline': Chem.MolFromSmarts('c1ccc2cnccc2c1'),
    'purine':       Chem.MolFromSmarts('c1ncc2[nH]cnc2n1'),

    # Fused polycyclic
    'anthracene':   Chem.MolFromSmarts('c1ccc2cc3ccccc3cc2c1'),
    'phenanthrene': Chem.MolFromSmarts('c1ccc2c(c1)ccc1ccccc12'),
    'acridine':     Chem.MolFromSmarts('c1ccc2nc3ccccc3cc2c1'),
}