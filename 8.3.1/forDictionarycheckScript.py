#!/usr/bin/python3
import subprocess
import os
import time
# Tekshiradigan faylning yo'li
script_path = "/home/haady/forDictionary.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "forDictionary-Flag.txt")

if not os.path.exists('/home/haady/checker_scripts.log'):
    open('/home/haady/checker_scripts.log', 'w').close()

with open('/home/haady/checker_scripts.log', "a") as file:
    file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {__file__} is running in background...\n")

# Infinite loop to check if the file exists
while True:
    # Check if the file exists
    if os.path.exists(script_path):
        try:
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)

            # Agar skript muvaffaqiyatli bajarilsa, flag faylini yaratish
            if result.returncode == 0 and result.stdout.strip() == "Name: Guts\nPersonality: gruff\nWeapon: Dragon Slayer\nArmor: Berserker Armor":
                # flag faylini yaratish
                if not os.path.exists(flag_dir):
                    os.makedirs(flag_dir)  # Agar flag papkasi mavjud bo'lmasa, yaratish
                with open(flag_file, "w") as file:
                    file.write("PYTHON{Jasorat_to'plamoqda}\n")
                break
        except Exception as e:
            pass
    time.sleep(60)
