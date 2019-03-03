## oscore.py - useful module of CLo.py
import os
import sys
import time

linuxos_banner = ("""
\033[0;36m _     ___ _   _ _   ___  __   ___  ____  
| |   |_ _| \ | | | | \ \/ /  / _ \/ ___| 
| |    | ||  \| | | | |\  /  | | | \___ \ 
| |___ | || |\  | |_| |/  \  | |_| |___) |
|_____|___|_| \_|\___//_/\_\  \___/|____/\033[0m                                           
 \033[0;32mCustom Linux Os Installation For Termux
\033[0;31m+=========================================+
| Author 	: Farhan Abdurahman       |
| Website 	: www.fsecurity7.com      |
\033[0;33m| Contact me 	: +6281222756005          |
| Version 	: V1.0                    |
+=========================================+\033[0m

""")
backtomenu_banner = ("""
    [99] Back to main menu
    [00] Exit the installation
""")
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def backtomenu_option():
        print (backtomenu_banner)
        backtomenu = raw_input("HaN7:~# ")

        if backtomenu == "99":
         restart_program()
        elif backtomenu == "00":
         sys.exit()
        else:
                print "\nERROR: Wrong Input"
                time.sleep(2)
                restart_program()

def banner():
        print linuxos_banner

def Kali_Linux():
        print ('\n###### Installing Kali Linux')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh")
        os.system("cd && bash kali.sh")
        print("=======================================")
        print("[+] Kali Linux installed successfully")
        print("[+] Type ./start-kali.sh to start")
        print("======================================,=")
        backtomenu_option()
        
def Kali_Nethunter():
        print ('\n###### Installing Kali Nethunter')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Nethunter/nethunter.sh")
        os.system("cd && bash nethunter.sh")
        print("=======================================")
        print("[+] Kali Nethunter installed successfully")
        print("[+] Type ./start-nethunter to start")
        print("======================================,=")
        backtomenu_option()
        
def Debian9():
        print ('\n###### Installing Debian 9')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Debian/debian.sh")
        os.system("cd && bash debian.sh")
        print("=======================================")
        print("[+] Debian 9 installed successfully")
        print("[+] Type ./start-debian to start")
        print("======================================,=")
        backtomenu_option()
        
def Ubuntu():
        print ('\n###### Installing Ubuntu')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh")
        os.system("cd && bash ubuntu.sh")
        print("=======================================")
        print("[+] Ubuntu installed successfully")
        print("[+] Type ./start-ubuntu to start")
        print("======================================,=")
        backtomenu_option()
        
def Fedora():
        print ('\n###### Installing Fedora')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Fedora/fedora.sh")
        os.system("cd && bash fedora.sh")
        print("=======================================")
        print("[+] Fedora installed successfully")
        print("[+] Type ./start-fedora to start")
        print("======================================,=")
        backtomenu_option()
        
def CentOs():
        print ('\n###### Installing CentOs')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/CentOS/centos.sh")
        os.system("cd && bash centos.sh")
        print("=======================================")
        print("[+] CentOs installed successfully")
        print("[+] Type ./start-centos to start")
        print("======================================,=")
        backtomenu_option()
        
def ParrotOs():
        print ('\n###### Installing Parrot Security Os')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Parrot/parrot.sh")
        os.system("cd && bash parrot.sh")
        print("=======================================")
        print("[+] Parrot Os installed successfully")
        print("[+] Type ./start-parrot to start")
        print("======================================,=")
        backtomenu_option()
        
def openSUSE_leap():
        print ('\n###### Installing OpenSUSU leap Os')
        os.system("cd")
        os.system("apt-get update -y")
        os.system("apt-get upgrade -y")
        os.system("apt-get install wget proot tar -y")
        os.system("cd && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/openSUSE/Leap/opensuse-leap.sh")
        os.system("cd && bash opensuse-leap.sh")
        print("=======================================")
        print("[+] openSUSE leap installed successfully")
        print("[+] Type ./start-leap to start")
        print("======================================,=")
        backtomenu_option()
