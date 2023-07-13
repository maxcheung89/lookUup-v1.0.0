#!/usr/bin/env python3

import platform
import os

def sys_check():

    # Check the operating system
    if platform.system() == "Windows":
        script_path = os.path.join("./scripts", "windows.py")
    elif platform.system() == "Linux":
        script_path = os.path.join("./scripts", "linux.py")
    else:
        print("Unsupported operating system.")
        exit()

    # Check if the script file exists
    if os.path.exists(script_path):
    # Execute the script
        os.system(f"python {script_path}")
    else:
        print("Script file not found.")

sys_check()