import subprocess
import os
import time
import logging

# Set up logging
logging.basicConfig(
    filename='/home/haady/checker.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Paths
script_path = "/home/haady/firstScript.py"
flag_dir = "/home/haady/flags"
flag_file = os.path.join(flag_dir, "firstScript-flag.txt")

# Main checking loop
while True:
    try:
        if os.path.exists(script_path):
            logging.info(f"Found script at {script_path}")
            result = subprocess.run(["python3", script_path], capture_output=True, text=True)
            
            logging.info(f"Script output: '{result.stdout.strip()}'")
            logging.info(f"Script return code: {result.returncode}")
            
            if result.stderr:
                logging.error(f"Script error output: {result.stderr}")

            if result.returncode == 0 and result.stdout.strip() == "Python qiziqarli!":
                logging.info("Script executed successfully with correct output")
                if not os.path.exists(flag_dir):
                    os.makedirs(flag_dir)
                    logging.info(f"Created flag directory at {flag_dir}")
                
                with open(flag_file, "w") as file:
                    file.write("PYTHON{B1Rinchi_Skript_Bajarildi!}\n\n")
                logging.info(f"Wrote flag to {flag_file}")
                break
            else:
                logging.warning("Script output didn't match expected output")
        else:
            logging.info(f"Waiting for script at {script_path}")
            
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
    
    time.sleep(30)