import json
import os

SAVE_FILE = "save.json"
DEFAULT_SAVE = {
    "player": {
        "vida": 100,
        "vida_max": 100,
        "mana": 50,
        "mana_max": 50,
        "level": 1,
        "xp": 0,
        "moedas": 0
    },

    "skills": {
        "espada": True,
        "fireball": False,
        "dash": False,
        "cura": False
    },

    "inventory": {
        "itens": []
    },

    "world": {
        "current_level": 1,
        "unlocked_levels": [1],
        "completed_levels": []
    }
}

def save_game(data):
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_game():
    if not os.path.exists(SAVE_FILE):
        save_game(DEFAULT_SAVE)
        return DEFAULT_SAVE.copy()

    with open(SAVE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)