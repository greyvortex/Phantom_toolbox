import os
import json

def log_hander():
    pass


def main():
    os.makedirs("logs", exist_ok=True)
    log_file_path = os.path.join("logs", "logfile.json")
