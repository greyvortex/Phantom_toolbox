import os
import time
from datetime import datetime


def log_manager(target,scan_type,open_ports,start_time,additional_info=""):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    log_data = f"Target: {target} \nScan Type: {scan_type} \nOpen Ports: {', '.join(map(str, open_ports))} \nScan Time: from {start_time} to {current_time}\nAdditional Info: {additional_info} \n"
    complete_log = f"Date:{current_date} | Time:{current_time}\n{log_data}\n\n"
    with open("temp_usr/phm_logs.log", "a") as log_file:
        log_file.write(complete_log)

log_manager("spsbbk.edu.in","Common Ports",[22,80,443],"12:04:01","I cant hack")