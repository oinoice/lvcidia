# config.py

# Represents the significance of each resource field. In the function
# total_earn_rate(data), the code calculates a weighted earning rate by
# multiplying each resource's intervalEarnRate by its weight. Fields with a
# higher weight have a more substantial influence on the total earning rate.
resource_weights = {
    8: 5,  # Obsidian
    5: 4,  # Gold
    3: 3,  # Ceramic
    4: 3,  # Chameleon
    1: 2,  # Black Titanium
    2: 2,  # Bronze
    9: 2,  # Silver
    7: 1,  # Hydrogen
    6: 1,  # Helium
}

# Helps in breaking ties when more than one field offers the maximum earning
# potential. It dictates which field should be chosen over others in such
# scenarios. Fields earlier in the list have higher importance.
value_hierarchy = [
    8,  # Obsidian
    5,  # Gold
    3,  # Ceramic
    4,  # Chameleon
    1,  # Black Titanium
    2,  # Bronze
    9,  # Silver
    7,  # Hydrogen
    6,  # Helium
]

# Labels for the RESOURCE EARNING SUMMARY table headers.
resource_codes = {
    1: "tit",
    2: "bro",
    3: "cer",
    4: "chm",
    5: "gld",
    6: "hel",
    7: "hyd",
    8: "obs",
    9: "sil",
}

# Labels for the HIGHEST YIELDING FIELD table.
resource_field_labels = {
    1: "Release",
    2: "Tentacula",
    3: "Mandelbulb",
    4: "After Life",
    5: "Galactic Lightfield",
    6: "Dragon Heart",
    7: "Intercore",
    8: "Cybernetic Core",
    9: "Infected",
    10: "Temporal Shifter",
    11: "Baeige",
    12: "Prism",
    13: "Chromatic Aberation",
    14: "Antiphysic",
}
