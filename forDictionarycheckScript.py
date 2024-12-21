import subprocess
import os

# Tekshiradigan faylning yo'li
script_path = "/home/haady/forDictionary.py"
flag_dir = "/home/haady/flag"
flag_file = os.path.join(flag_dir, "forDictionary-Flag.txt")

# Agar fayl mavjud bo'lsa, skriptni ishga tushirish
if os.path.exists(script_path):
    try:
        result = subprocess.run(["python3", script_path], capture_output=True, text=True)

        # Agar skript muvaffaqiyatli bajarilsa, flag faylini yaratish
        if result.returncode == 0 and result.stdout.strip() == "Name: Guts\nPersonality: gruff\nWeapon: Dragon Slayer\nArmor: Berserker Armor":
            # flag faylini yaratish
            if not os.path.exists(flag_dir):
                os.makedirs(flag_dir)  # Agar flag papkasi mavjud bo'lmasa, yaratish
            with open(flag_file, "w") as file:
                file.write("PYTHON{Jasorat_to'plamoqda}")
    except Exception as e:
        pass
