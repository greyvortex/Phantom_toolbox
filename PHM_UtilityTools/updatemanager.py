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
    file_path = "temp_usr/hash"
    if os.path.exists(file_path):
        with open(file_path,"r") as file:
            hash_data = file.read()
            lines = hash_data.splitlines()
            last_hash = lines[-1] if lines else None
            print(f"Last Hash: {last_hash}")
            print(f"New Hash: {new_hash}")
            if last_hash == new_hash:
                print("No update available.")
                return 0
            elif(last_hash == None):
                with open(file_path,"a") as file:
                    file.write(new_hash)
                print("First run , no updates available.")
                return 0
            else:
                with open(file_path,"a") as file:
                    file.write("\n"+new_hash)
                print("Update available.")
        return 1
    else:
        os.makedirs("temp_usr",exist_ok=True)
        with open(file_path,"a") as file:
            file.write(new_hash)
        return 0


check = comparator(get_latest_commit_hash())
print(check)
print(get_latest_commit_hash())
