## CLo.py - CLo v1.0

##
import os
import sys
from time import sleep as timeout
from core.oscore import *

def main():
        banner()
        print ("\033[0;32m[01] OS Menu Installation")
	print ("\033[0;31m[02] Desktop Environment")
        print ("\033[0;31m[03] Exit the Program\033[0m")
	print ("\n")
        clo = raw_input ("\033[0;32mHaN7:~# ")

        if clo == "1" or clo == "01":
            print ("\n    \033[0;36m[01] Kali Linux")
            print ("    [02] Kali Nethunter")
            print ("    [03] Debian 9")
            print ("    [04] Ubuntu")
            print ("    [05] Fedora")
            print ("    [06] CentOs")
            print ("    [07] Parrot Sec Os")
            print ("    [08] openSUSE_leap")
            print ("    [00] Back to main menu")
	    print ("\n")
            customosinstall = raw_input("HaN7:~#\033[0m ")

            if customosinstall == "01" or customosinstall == "1":
                    Kali_Linux()
            elif customosinstall == "02" or customosinstall == "2":
                    Kali_Nethunter()
            elif customosinstall == "03" or customosinstall == "3":
                    Debian9()
            elif customosinstall == "04" or customosinstall == "4":
                    Ubuntu()
            elif customosinstall == "05" or customosinstall == "5":
                    Fedora()
            elif customosinstall == "06" or customosinstall == "6":
                    CentOs()
            elif customosinstall == "07" or customosinstall == "7":
                    ParrotOs()
            elif customosinstall == "08" or customosinstall == "8":
                    openSUSE_leap()
            elif customosinstall == "00" or customosinstall == "0":
                    restart_program()
            else:
                    print("\nERROR: Wrong Input")
                    timeout(2)
                    restart_program()

	elif clo == "02" or clo == "2":
            banner()
	    print ("\n      [01] DE Ubuntu")
            print("     [02] DE Debian")
            print("     [03] DE Kali Linux")
            print("     [04] DE Fedora")
            print("     [05] DE Parrot Sec")
            print("     [06] DE Arch Linux")
            print("     [00] EXIT")
            chose = raw_input("HaN7:~# ")

            if chose == "01" or chose == "1":
                DE_Ubuntu()
            elif chose == "02" or chose == "2":
                DE_Debian()
            elif chose == "03" or chose == "3"
                DE_Kali()
            elif chose == "04" or chose == "4":
                DE_Fedora()
            elif chose == "05" or chose == "5":
                DE_Parrot()
            elif chose == "06" or chose == "6":
                DE_ARCH()
            elif chose == "00" or chose == "0":
                restart_program
            else:
                    print"\nERROR: Wrong Input"
                    timeout(2)
                    restart_program()
                    
        elif clo == "03" or clo == "3":
            sys.exit()

        else:
            print("\nERROR: Wrong Input")
            timeout(2)
            restart_program()

if __name__ == "__main__":
        main()
            
