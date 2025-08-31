from pathlib import Path
import json, shutil

MAIN_DIR = Path(__file__).resolve().parent
CONFIG = MAIN_DIR / "config.json"

with open(CONFIG, "r") as config_file:
    config = json.load(config_file)

dir = MAIN_DIR if not config["PARENT_DIR"] else config["PARENT_DIR"]
