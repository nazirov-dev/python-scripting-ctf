import subprocess
import os

# Tekshiradigan faylning yo'li
script_path = "/home/haady/typeCasting.py"
flag_dir = "/home/haady/flag"
flag_file = os.path.join(flag_dir, "typeCasting-Flag.txt")

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
                file.write("PYTHON{Gr1t_b1l@n_Tur_@yl@nt1r1sh}")
    except Exception as e:
        pass
