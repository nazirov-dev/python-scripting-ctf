#!/usr/bin/python3
import subprocess
import os
import time
# Tekshiradigan faylning yo'li
script_path = "/home/haady/createList.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "createList-Flag.txt")

# Infinite loop to check file and write flag
while True:
    # Agar fayl mavjud bo'lsa, skriptni ishga tushirish
    if os.path.exists(script_path):
        try:
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)
            # Agar skript muvaffaqiyatli bajarilsa, flag faylini yaratish
            result_text = result.stdout.strip().lower()
            print(result_text)
            if result.returncode == 0 and (result_text == '["guts", "griffith", "casca"]' or result_text == "['guts', 'griffith', 'casca']"):
            # flag faylini yaratish
                if not os.path.exists(flag_dir):
                    os.makedirs(flag_dir)  # Agar flag papkasi mavjud bo'lmasa, yaratish
                with open(flag_file, "w") as file:
                        file.write("PYTHON{B0l1ml@r_0r@51d@g1_4_n1m@}\n")
                break
        except Exception as e:
            pass
    time.sleep(30)
