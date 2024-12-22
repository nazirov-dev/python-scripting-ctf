import ast
import subprocess
import os

# Tekshiradigan faylning yo'li
script_path = "/home/haady/nameAge.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "nameAge-Flag.txt")

# int(input()) konstruktsiyasini tekshirish
def check_int_input_usage(file_path):
    try:
        with open(file_path, "r") as file:
            code = file.read()
        tree = ast.parse(code)

        # AST daraxtida int(input()) ni izlash
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call) and
                isinstance(node.func, ast.Name) and node.func.id == "int" and
                len(node.args) == 1 and
                isinstance(node.args[0], ast.Call) and
                isinstance(node.args[0].func, ast.Name) and node.args[0].func.id == "input"
            ):
                return True
        return False
    except Exception as e:
        return False

# int(input()) mavjudligini tekshirish va skriptni ishga tushirish
if check_int_input_usage(script_path):
    try:
        # Skriptni ishga tushirish va input berish
        result = subprocess.run(
            ["python3", script_path],
            input="Haady\n24\n",
            capture_output=True,
            text=True
        )
        if result.returncode == 0 :
            # flag faylini yaratish
            if not os.path.exists(flag_dir):
                os.makedirs(flag_dir)
            with open(flag_file, "w") as file:
                file.write("PYTHON{Foydalanuvchini_so'rov_berish}\n")
        print(result.stdout.strip())
    except Exception as e:
        pass

