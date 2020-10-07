#!/usr/bin/python3
import subprocess as sp
from MAC_CHANGER_COMPLEX import macchanger
from ARP_Spoofer import arp_spoof
from Network_Scanner_Basic import net_scan
# from DNS_Spoofer import dns_spooof
from packet_sniffer import sniffer
from arp_spoof_detector import arp_detect
from malware import keylog
try:
    def options():
        print("1. [-]Change Mac and go anonymous !")
        print("2. [-]Scan your Network for connected devices !")
        print("3. [-]ARP Spoof the target !")
        print("4. [-]Man in the Middle Attacks !")
        print("5. [-]Intercepting Files !")
        print("6. [-]Bypass HTTPS !")
        print("7. [-]ARP Spoof detector !")
        print("8. [-]Malwares !")
        print("\nPress 0 to stop !")
        n = int(input("\nSelect carefully what you want to do :"))
        if n == 0:
            print("\n\nGood, better not to mess with the things you don't understand !\n\n")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        elif n == 1:
            macchanger()
            print("\n\nSo what's next ?\n\n")
            options()
        elif n == 2:
            net_scan()
            print("\n\nWhat next?\n\n")
            options()
        elif n ==3:
            arp_spoof()
            print("\n\nWhat next?\n\n")
            options()
        elif n ==4:
            dns_spoof()
            print("\n\nWhat next?\n\n")
            options()
        elif n ==5:
            sniffer()
            print("\n\nWhat next?\n\n")
            options()
        elif n ==7:
            arp_detect()
            print("\n\nWhat next?\n\n")
            options()
        elif n ==8:
            keylog()
            print("\n\nWhat next?\n\n")
            options()
        else:
            print("\n\nPlease select the correct option!\n\n")
            options()
    def show():
        # sp.call("sudo apt install figlet", shell = True)
        sp.call("figlet websploit -c", shell=True)
        print("\n-*-*-*-*-*-*--*-*-*-*--*-*-*--*-*-*-*-*--*-*-*-*--*-*-*--*-*-*--*-*-*--*-*-*-*-*-")
        print("\n\n\t\tA linux system application software for penetration testing. ")
        print("\n\nVer 1.0.0 developed by Inder, Jaspreet and Jasmine.\n")
        print("No show without root so, run as root or don't !\n\n")
        options()

    show()
except KeyboardInterrupt:
    print("\n\n[!] Ctrl + C detected. Goodbye, see ya again!\n\n")