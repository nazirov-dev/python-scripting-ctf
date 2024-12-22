#!/usr/bin/python3
import subprocess
import os
import time

script_path = "/home/haady/firstScript.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "firstScript-flag.txt")

while True:
    try:
        if os.path.exists(script_path):
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)

            if result.returncode == 0 and result.stdout.strip() == "Python qiziqarli!":
                if not os.path.exists(flag_dir):
                    os.makedirs(flag_dir)
                
                with open(flag_file, "w") as file:
                    file.write("PYTHON{B1Rinchi_Skript_Bajarildi!}\n\n")
                break
    except Exception as e:
        pass
    
    time.sleep(30)