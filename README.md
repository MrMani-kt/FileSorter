# 📂 Python File Organizer

A smart and efficient Python tool to **automatically organize** cluttered folders. This script scans a directory and sorts files into dedicated folders based on their file extensions (e.g., .jpg, .pdf, .docx).

## 🚀 Features
- **Auto-Categorization:** Group files by their extensions automatically.
- **Smart Directory Creation:** Creates a new folder for each file type if it doesn't already exist.
- **Regex Integration:** Uses Regular Expressions for precise extension extraction.
- **Modern Path Handling:** Built with `pathlib` for cross-platform compatibility.

## 🛠 Prerequisites
This project uses **Python Standard Libraries** only. You do **not** need to install any external packages (no `pip install` required).

**Libraries used:**
- `pathlib`: For object-oriented filesystem paths.
- `re`: For regex-based extension parsing.
- `shutil`: For high-level file operations (moving files).

## ⚙️ How to Setup
To make this script work on your system, you need to update the directory paths in the code:

1. Open `main.py`.
2. Locate the following placeholders and replace them with your actual system paths:
   - `source_dir`: The folder you want to clean up.
   - `destination_folder`: Where you want the organized folders to be created.

> **Tip:** Use raw strings for Windows paths to avoid errors, like this:  
> `Path(r"C:\Users\YourName\Downloads")`

## 🔍 How it Works
1. **Scanning:** The script iterates through every file in the specified source directory.
2. **Detection:** It uses Regex to identify the file extension (e.g., it extracts `png` from `image.png`).
3. **Creation:** It checks if a folder named after that extension exists. If not, it creates it.
4. **Moving:** It moves the file from the root folder into the corresponding extension folder.

## ⚠️ Important Notes
- **Move vs Copy:** This script **moves** files. It does not create copies, so your original folder will be emptied of files and replaced by organized sub-folders.
- **Extensionless Files:** Files without extensions are skipped to prevent errors.

## 🤝 Contributing
Feel free to fork this project and submit a Pull Request if you'd like to add features like a GUI or a "dry run" mode!