import subprocess
import os

# Tekshirish uchun fayl va flag yo'llari
script_path = "/home/haady/webDownloader.py"
index_path = "/var/www/html/index.html"  # Apache index.html yo'li
flag_dir = "/home/haady/flag"
flag_file = os.path.join(flag_dir, "webDownloader-Flag.txt")

# Flag matni
flag_text = "PYTHON{Veb-sahifalarni_ichkariga_olish_xuddi_qo'shni_o'rgimchak-odamdek}"

# Apache index.html mazmunini o'qish
def read_index_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"index.html faylini o'qishda xatolik: {e}")
        return None

# webDownloader.py skriptini ishga tushirish va natijasini olish
def run_script(script_path):
    try:
        result = subprocess.run(["python3", script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"Skript bajarishda xatolik: {result.stderr}")
            return None
    except Exception as e:
        print(f"Skriptni ishga tushirishda xatolik: {e}")
        return None

# Tekshiruv va flag faylini yaratish
def create_flag_if_matches():
    index_content = read_index_file(index_path)
    if index_content is None:
        return

    script_output = run_script(script_path)
    if script_output is None:
        return

    # Mazmunni solishtirish
    if index_content.strip() == script_output.strip():
        if not os.path.exists(flag_dir):
            os.makedirs(flag_dir)  # Flag papkasini yaratish
        with open(flag_file, "w") as file:
            file.write(flag_text)
        print(f"Flag fayli yaratildi: {flag_file}")
    else:
        print("Mazmunlar mos emas. Flag yaratilmaydi.")

# Funksiyani ishga tushirish
create_flag_if_matches()

