# ArchipelagoConstants.py

# --- Validation Constants ---
VALID_GP_TYPES = [
    "UNITCLASS_SCIENTIST", 
    "UNITCLASS_ENGINEER", 
    "UNITCLASS_PROPHET", 
    "UNITCLASS_ARTIST", 
    "UNITCLASS_MERCHANT", 
    "UNITCLASS_GREAT_GENERAL", 
    "UNITCLASS_GREAT_SPY"
]

TECH_TRANSLATION_DICT = {
    "Agriculture" : "TECH_AGRICULTURE"
}

TECH_LOCATION_MAP = {
    "TECH_AGRICULTURE":   {"location": "Tech_Agriculture"},
    "TECH_MINING":   {"location": "Tech_Mining"},
    "TECH_MYSTICISM":     {"location": "Tech_Mysticism"},
    "TECH_BRONZE_WORKING": {"location": "Tech_BronzeWorking"},
    "TECH_IRON_WORKING":   {"location": "Tech_IronWorking"},
    "TECH_RIFLING":        {"location": "Tech_Rifling"},
}
