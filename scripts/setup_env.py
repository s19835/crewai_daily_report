import os
import subprocess

def install_requirements():
    """Install the required pakages from requirements.txt"""
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Successfully installed Requirements.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")

def create_folders():
    """Create neccessary folders for the Project"""
    folders = ["src/data/drafts", "src/data/final", "src/data/research", "src/logs"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print(f"Successfully created neccessary folders")

def main():
    install_requirements()
    create_folders()

if __name__ == "__main__":
    main()