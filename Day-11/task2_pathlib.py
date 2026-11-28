from pathlib import Path

# --- Task 1: Check if 'backup' folder exists; if not, create it ---
print("--- Task 1: Backup Folder Check ---")
backup_folder = Path("backup")

if not backup_folder.exists():
    backup_folder.mkdir()
    print("Created 'backup' folder.")
else:
    print("'backup' folder already exists.")

# --- Task 2: Create 'notes.txt' if missing, then print its size and suffix ---
print("\n--- Task 2: File Size & Suffix ---")
notes_file = Path("notes.txt")

if not notes_file.exists():
    notes_file.write_text("These are sample notes for Day 11 pathlib task.")

if notes_file.exists():
    print("File Name:", notes_file.name)
    print("File Size (bytes):", notes_file.stat().st_size)
    print("File Suffix (extension):", notes_file.suffix)

# --- Task 3: Convert a relative path to its absolute (full) path ---
print("\n--- Task 3: Absolute Path ---")
relative_path = Path("data/raw_data.txt")
print("Relative Path:", relative_path)
print("Absolute Path:", relative_path.resolve())