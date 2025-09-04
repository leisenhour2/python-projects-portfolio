from pathlib import Path
import json, shutil

# Get the folder where this script lives
PARENT_DIR = Path(__file__).resolve().parent

# Load settings from config.json
with open(PARENT_DIR / "config.json", "r") as jsonfile:
    file_dir = json.load(jsonfile)


# Function to create a folder if it doesn't exist
def create_folder(folder) -> Path:
    f = Path(folder)
    f.mkdir(parents=True, exist_ok=True)
    return f


# Input and output folders
INPUT = create_folder(file_dir["Input"])
OUTPUT = create_folder(file_dir["Output"])

# Special folders for unrecognized files
MISC = create_folder(OUTPUT / "Misc")
FILES = create_folder(OUTPUT / "Files")

# File type categories from config.json
FILETYPES = file_dir["FileTypes"]

# Create each category folder
for key in FILETYPES.keys():
    create_folder(OUTPUT / key)

# Go through everything in INPUT
for item in INPUT.iterdir():
    if item.is_dir():
        # If it's a folder, move it to Misc
        shutil.move(str(item), str(MISC / item.name))

    elif item.is_file():
        ext = item.suffix.lower()  # e.g. ".png"

        # If file has no extension
        if not ext:
            shutil.move(str(item), str(FILES / item.name))
            continue

        # Try to match the extension with categories
        moved = False
        for key, value in FILETYPES.items():
            if ext in value:  # config already has "." in extensions
                shutil.move(str(item), str((OUTPUT / key) / item.name))
                moved = True
                break

        # If no match was found, move to Misc
        if not moved:
            shutil.move(str(item), str(MISC / item.name))
