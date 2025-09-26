# File Organizer

A simple Python tool to automatically organize files in a folder by type (Images, Documents, Videos, Music, Others).

## Features
- Automatically creates folders for each file type
- Moves files into their respective folders based on extension
- Handles duplicate filenames by renaming
- Logs actions to `organizer_log.txt`

## Supported File Types
- Images: `.jpg`, `.jpeg`, `.png`, `.gif`
- Documents: `.pdf`, `.docx`, `.txt`, `.csv`, `.json`
- Videos: `.mp4`, `.mkv`, `.avi`, `.mov`
- Music: `.mp3`, `.m4a`, `.wav`
- Others: All other file types

## Requirements
- Python 3.x

## Usage
1. Set your target folder path in the script:
   ```python
   folder_path = r"C:\path\to\your\folder"
   ```
2. Log will enter date and time automaticly add any additional info if you want.
   ```tool.log("👉Here👈")

3. Run the script:
   ```
   python file_organizer.py
   ```
4. Files will be organized into subfolders inside your target folder.

---
This script is for personal and educational use. Always back up important files before running automation scripts.
