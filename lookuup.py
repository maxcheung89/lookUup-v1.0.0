#!/usr/bin/env python3
import platform
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


def main():
    # Check the machine architecture
    arch = platform.machine()

    # Choose the correct file to run based on the architecture
    if arch == "x86_64":
        filename = "./scripts/linuxx86"
    elif arch == "aarch64":
        filename = "./scripts/linuxarm64"
    else:
        print(f"Unsupported architecture: {arch}")
        return

    # Run the selected file
    subprocess.run([filename])

if __name__ == "__main__":
    main()