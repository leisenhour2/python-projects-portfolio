# File Organizer (Beginner Project)

This is a simple Python script that organizes files into folders based on their type.
It uses a `config.json` file so you can easily change the input/output folders and the file categories.

---

## How It Works

1. Put the files you want to organize into the **Input** folder (set in `config.json`).
2. Run the script with Python.
3. The script will:
   - Create category folders (like `Image_Files`, `Video_Files`, `PDF_Files`, etc.)
   - Move each file into the right category based on its extension.
   - Put folders or unknown file types into the `Misc` folder.
   - Put files with **no extension** into the `Files` folder.

---

## Example `config.json`

```json
{
  "Input": "C:/Users/YourName/Desktop/New folder",
  "Output": "C:/Users/YourName/Desktop/Organized",
  "FileTypes": {
    "Image_Files": [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
    "Video_Files": [".mp4", ".avi", ".mov"],
    "Audio_Files": [".mp3", ".wav", ".ogg"],
    "Word_Files": [".doc", ".docx", ".txt", ".rtf"],
    "PDF_Files": [".pdf"],
    "Spreadsheet_Files": [".xls", ".xlsx", ".csv"],
    "Presentation_Files": [".ppt", ".pptx"],
    "Compressed_Files": [".zip", ".rar"],
    "Database_Files": [".accdb", ".mdb"]
  }
}
```
