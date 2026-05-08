HSAB_rules = {
    # --- NUCLÉOPHILES MOUS (polarisables) ---
    "thiol":            {"nucleo": -0.80, "electro":  0.00},  # pKa ~9 → non déprotoné à pH7
    "sulfide":          {"nucleo": -0.65, "electro":  0.00},
    "isothiocyanate":   {"nucleo": -0.50, "electro":  0.00},
 
    # --- AMINES → protonées à pH 7 (pKa conjugate acid ~9-11 > 7) → mauvais nucléophiles ---
    "primary amine":    {"nucleo":  0.10, "electro":  0.00},  # NH3+ → mauvais nucléophile
    "secondary amine":  {"nucleo":  0.10, "electro":  0.00},  # NH2+ → mauvais nucléophile
    "tertiary amine":   {"nucleo":  0.10, "electro":  0.00},  # NH+  → mauvais nucléophile
    "imine":            {"nucleo": -0.10, "electro":  0.00},  # pKa ~5-7 → partiellement protoné
 
    # --- OXYGÈNES → non déprotonés à pH 7 ---
    "alcohol":          {"nucleo": -0.55, "electro":  0.00},  # pKa ~17 → neutre à pH7
    "phenol":           {"nucleo": -0.20, "electro":  0.00},  # pKa ~9  → neutre à pH7
    "ether":            {"nucleo": -0.15, "electro":  0.00},
    "alkene":           {"nucleo": -0.20, "electro":  0.00},
 
    # --- ACIDES → carboxylic_acid déprotoné à pH 7 (pKa ~4-5 < 7 → COO-) ---
    "carboxylic_acid":  {"nucleo": -0.80, "electro":  0.30},  # COO- à pH7 → bon nucléophile
 
    # --- ÉLECTROPHILES ---
    "acyl_chloride":    {"nucleo":  0.00, "electro":  0.90},
    "anhydride":        {"nucleo":  0.00, "electro":  0.80},
    "aldehyde":         {"nucleo":  0.00, "electro":  0.70},
    "ketone":           {"nucleo":  0.00, "electro":  0.60},
    "ester":            {"nucleo":  0.00, "electro":  0.55},
    "amide":            {"nucleo":  0.25, "electro":  0.15},
    "nitro":            {"nucleo":  0.00, "electro":  0.40},
    "nitrile":          {"nucleo":  0.00, "electro":  0.50},
    "isocyanate":       {"nucleo":  0.00, "electro":  0.70},
    "alkyl halide":     {"nucleo":  0.00, "electro":  0.50},
    "epoxide":          {"nucleo":  0.00, "electro":  0.65},
    "sulfonyl chloride":{"nucleo":  0.00, "electro":  0.85},
    "sulfoxide":        {"nucleo":  0.00, "electro":  0.40},
    "sulfone":          {"nucleo":  0.00, "electro":  0.45},
    "lactone":          {"nucleo":  0.00, "electro":  0.60},
    "lactam":           {"nucleo":  0.00, "electro":  0.75},
}
 