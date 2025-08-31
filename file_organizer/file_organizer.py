from pathlib import Path
import json, shutil

PARENT_DIR = Path(__file__).resolve().parent
CONFIGURATION = PARENT_DIR / "config.json"
with open(CONFIGURATION, "r") as config_file:
    config = json.load(config_file)

INPUT = PARENT_DIR / "INPUT"
OUTPUT = PARENT_DIR / "OUTPUT"
# folder.mkdir(parents=True, exist_ok=True)


def creates_folder(folder) -> Path:
    f = Path(folder)
    f.mkdir(parents=True, exist_ok=True)
    return f


creates_folder(INPUT)
creates_folder(OUTPUT)

for key in config.keys():
    creates_folder(OUTPUT / key)
