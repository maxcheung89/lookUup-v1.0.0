#!/usr/bin/env python3

import platform
import os
import subprocess

def banner():
    print("**********************************************************************\n*                                                                    *\n*    BE CAREFUL!! MAKE SURE YOU KNOW THE PASSWORD BEFORE RUN         *\n*   You will take full responsibility if you choose to countinue     *\n*                                                                    *\n*    Enter Your Password Down Below if You Wish to Countinue!        *\n*                                                                    *\n**********************************************************************")

banner()

def sys_check():

    # Check the operating system
    if platform.system() == "Windows":
        script_path = os.path.join("./scripts", "windows.py")
    elif platform.system() == "Linux":
        executable_path = "./scripts/linux"
        script_path = subprocess.run(executable_path)
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