import subprocess
import os
import time

# Tekshiradigan faylning yo'li
script_path = "/home/haady/firstScript.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "firstScript-flag.txt")

# Agar fayl mavjud bo'lsa, skriptni ishga tushirish
if os.path.exists(script_path):
    while True:
        try:
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)

            # Agar skript muvaffaqiyatli bajarilsa, flag faylini yaratish
            if result.returncode == 0 and result.stdout.strip() == "Python qiziqarli!":
                # flag faylini yaratish
                if not os.path.exists(flag_dir):
                    os.makedirs(flag_dir)  # Agar flag papkasi mavjud bo'lmasa, yaratish
                with open(flag_file, "w") as file:
                    file.write("PYTHON{B1Rinchi_Skript_Bajarildi!}\n")
                break
        except Exception as e:
            pass
        time.sleep(30)