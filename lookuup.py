#!/usr/bin/env python3

import subprocess

def get_linux_distribution():
    with open('/etc/os-release') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('PRETTY_NAME'):
            distro = line.split('=')[1].strip().strip('"')
            return distro
    return "Unknown Distribution"

print(f'\nHey! We Are Runing On: {get_linux_distribution()}\n')


def banner():
    print("**********************************************************************\n*                                                                    *\n*    BE CAREFUL!! MAKE SURE YOU KNOW THE PASSWORD BEFORE RUN         *\n*   You will take full responsibility if you choose to countinue     *\n*                                                                    *\n*    Enter Your Password Down Below if You Wish to Countinue!        *\n*                                                                    *\n**********************************************************************")

banner()



# specify the path to your executable file
executable_path = "./scripts/linux"

# run the executable
process = subprocess.run(executable_path)
