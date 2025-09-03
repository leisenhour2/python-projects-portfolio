from pathlib import Path
import json, shutil

PARENT_DIR = Path(__file__).resolve().parent
CONFIGURATION = PARENT_DIR / "config.json"

with open(CONFIGURATION, "r") as config_file:
    config = json.load(config_file)

INPUT = PARENT_DIR / "INPUT"
OUTPUT = PARENT_DIR / "OUTPUT"


def creates_folder(folder) -> Path:
    f = Path(folder)
    f.mkdir(parents=True, exist_ok=True)
    return f


# Make sure folders exist
creates_folder(INPUT)
creates_folder(OUTPUT)
creates_folder(OUTPUT / "Misc")
creates_folder(OUTPUT / "Files")
for key in config.keys():
    creates_folder(OUTPUT / key)


# Sort files
for file in INPUT.iterdir():
    if file.is_file():
        ext = file.suffix.lower()

        # No extension → Files
        if not ext:
            shutil.move(str(file), OUTPUT / "Files" / file.name)
            continue

        # Try to match extension in config
        moved = False
        for key, value in config.items():
            if ext in value:
                shutil.move(str(file), OUTPUT / key / file.name)
                moved = True
                break

        # If no match at all → Misc
        if not moved:
            shutil.move(str(file), OUTPUT / "Misc" / file.name)
