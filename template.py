import os

# ===============================
# FOLDER STRUCTURE (RELATIVE)
# ===============================
STRUCTURE = {
    "config": ["__init__.py", "settings.py"],
    "inference": ["__init__.py", "roboflow_client.py"],
    "processing": ["__init__.py", "predictions.py", "visualization.py"],
    "video": ["__init__.py", "video_io.py"],
    "": ["main.py", "requirements.txt", "README.md"]
}

# ===============================
# CREATE STRUCTURE IN CURRENT DIR
# ===============================
def create_structure():
    base_path = os.getcwd()

    for folder, files in STRUCTURE.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")
                print(f"Created: {file_path}")

    print("\n✅ Folder structure created in current directory")

# ===============================
# ENTRY POINT
# ===============================
if __name__ == "__main__":
    create_structure()
