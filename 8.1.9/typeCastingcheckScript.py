#!/usr/bin/python3
import subprocess
import os
import time

# Tekshiradigan faylning yo'li
script_path = "/home/haady/typeCasting.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "typeCasting-Flag.txt")

if not os.path.exists('/home/haady/checker_scripts.log'):
    open('/home/haady/checker_scripts.log', 'w').close()

with open('/home/haady/checker_scripts.log', "a") as file:
    file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {__file__} is running in background...\n")

# Infinite loop to check file and write flag
while True:
    # Agar fayl mavjud bo'lsa, skriptni ishga tushirish
    if os.path.exists(script_path):
        try:
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)

            # Agar skript muvaffaqiyatli bajarilsa, flag faylini yaratish
            if result.returncode == 0 and result.stdout.strip() == 'The manga, "Berserk," was written by Kentaro Miura and was premiered as a prototype in the year 1988':
                # flag faylini yaratish
                if not os.path.exists(flag_dir):
                    os.makedirs(flag_dir)  # Agar flag papkasi mavjud bo'lmasa, yaratish
                with open(flag_file, "w") as file:
                    file.write("PYTHON{Gr1t_b1l@n_Tur_@yl@nt1r1sh}\n")
                break
        except Exception as e:
            pass
    time.sleep(60)
