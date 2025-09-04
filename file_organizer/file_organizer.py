from pathlib import Path
import json, shutil

PARENT_DIR = Path(__file__).resolve().parent

with open(PARENT_DIR / "config.json", "r") as jsonfile:
    file_dir = json.load(jsonfile)


def create_folder(folder) -> Path:
    f = Path(folder)
    f.mkdir(parents=True, exist_ok=True)
    return Path(f)


INPUT = create_folder(file_dir["Input"])
OUTPUT = create_folder(file_dir["Output"])

MISC = create_folder(OUTPUT / "Misc")
FILES = create_folder(OUTPUT / "Files")
FILETYPES = file_dir["FileTypes"]

for key in FILETYPES.keys():
    create_folder(OUTPUT / key)

for item in INPUT.iterdir():
    if item.is_dir():
        shutil.move(str(item), OUTPUT / "Misc" / item.name)
    if item.is_file():
        ext = item.suffix.lower()
        if not ext:
            shutil.move(str(item), OUTPUT / "Files" / item.name)
            continue
        for key, value in FILETYPES.items():
            moved = False
            if ext in value:
                shutil.move(str(item), OUTPUT / key / item.name)
                moved = True
                break
        if not moved:
            shutil.move(str(item), OUTPUT / "Misc" / item.name)
