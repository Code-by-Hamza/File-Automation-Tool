import os, shutil
from datetime import datetime

class FileOrganize:
    def __init__(self,folder):
        self.folder = folder
        self.extensions = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt", ".csv", ".json"],
            "Videos": [".mp4", ".mkv", ".avi", ".mov"],
            "Music": [".mp3", ".m4a", ".wav"],
            "Others": []
        }
    #Create Folders
    def create_folders(self):
        for folder_name in self.extensions.keys():
            path = os.path.join(self.folder, folder_name)
            os.makedirs(path, exist_ok=True)
    #Move & Rename Files
    def organize(self):
        for file in os.listdir(self.folder):
            file_path = os.path.join(self.folder, file)
            if os.path.isfile(file_path):
                moved = False
                for folder_name,exts in self.extensions.items():
                    if any(file.lower().endswith(ext) for ext in exts):
                        new_path = os.path.join(self.folder, folder_name, file)
                        new_path = self.rename_if_exists(new_path)
                        shutil.move(file_path, new_path)
                        moved = True
                        break
                if not moved:
                    new_path = os.path.join(self.folder, "Others", file)
                    new_path = self.rename_if_exists(new_path)
                    shutil.move(file_path, new_path)
    #Rename if file exists
    def rename_if_exists(self,path):
        base, ext = os.path.splitext(path)
        counter = 1
        while os.path.exists(path):
            path = f"{base}-{counter}{ext}"
            counter += 1
        return path
    
    #loging Actions
    def log(self, message):
        with open("organizer_log.txt", "a") as f:
            f.write(f"{datetime.now()} - {message}\n")


#Example Usuage
if __name__ == "__main__":
    folder_path = r"C:\path\to\your\folder" #change this to your path

    tool = FileOrganize(folder_path)
    tool.create_folders()
    tool.organize()
    tool.log("example text...") #add any aditional info here
    print("Files Organized Successfully!")