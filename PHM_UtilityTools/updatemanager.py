import requests
import json
import io
import zipfile
import os
import shutil


def get_latest_commit_hash():
    url = f"https://api.github.com/repos/The-Phantom-Project/Phantom_Toolbox/commits/main"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["sha"]
    else:
        print("Failed to fetch commit info:", response.status_code)
        return None

def comparator(new_hash):
    file_path = "temp_usr/hash.txt"
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            hash_data = file.read()
            lines = hash_data.splitlines()
            last_hash = lines[-1] if lines else None
            if last_hash == new_hash:
                return 0
            elif(last_hash == None):
                with open(file_path,"a") as file:
                    file.write(new_hash)
                return 0
            else:
                with open(file_path,"a") as file:
                    file.write("\n"+new_hash)
            return 1
    else:
        os.makedirs("temp_usr",exist_ok=True)
        with open(file_path,"a") as file:
            file.write(new_hash)
        return 0

def Downloader():
    url = "https://github.com/The-Phantom-Project/Phantom_toolbox/archive/refs/heads/main.zip"
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall("temp_usr")
    

def manual_reader():
    with open("temp_usr/Phantom_Toolbox-main/update_info.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith("Updated:"):
                updates = line[len("Updated:"):].strip().split(",")
                for update in updates:
                        src = os.path.join("temp_usr/Phantom_Toolbox-main", update)
                        dst = os.path.join(".", update)
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        if os.path.isdir(src):
                            shutil.rmtree(dst, ignore_errors=True)
                        else:
                            os.remove(dst)

                        if os.path.isdir(src):
                            shutil.copytree(src, dst)
                        else:
                            shutil.copy2(src, dst)

            elif line.startswith("Added:"):
                additions = line[len("Added:"):].strip().split(",")
                for addition in additions:
                    src_dst = addition.strip().split("->")
                    if len(src_dst) == 2:
                        src = os.path.join("temp_usr/Phantom_Toolbox-main", src_dst[0].strip())
                        dst = os.path.join(".", src_dst[1].strip())
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        if os.path.isdir(src):
                            shutil.copytree(src, dst)
                        else:
                            shutil.copy2(src, dst)

            elif line.startswith("Deleted:"):
                deletions = line[len("Deleted:"):].strip().split(",")
                for deletion in deletions:
                    file_to_delete = os.path.join(".", deletion.strip())
                    if os.path.exists(file_to_delete):
                        if os.path.isdir(file_to_delete):
                            shutil.rmtree(file_to_delete)
                        else:
                            os.remove(file_to_delete)
            else:
                pass

def update_workflow():
        Latest_hash = get_latest_commit_hash()
        if Latest_hash:
            status = comparator(Latest_hash)
            if status == 1:
                print("Downloading update...")
                Downloader()
                print("Applying update...")
                manual_reader()
                print("Update applied successfully.")
            elif status == 0:
                print("No updates available or first run setup completed.")
            else:
                print("An error occurred during the update process.")


def sudo(lvl):
    if lvl == 1:
        update_workflow
    else:
        os.remove("update_manager")