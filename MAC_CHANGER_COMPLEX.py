#!/usr/bin/python3

import subprocess
import re
import optparse

def macchanger():

    def get_arguments():

        """"Getting the interface name and the new mac address"""
        interface = input("\n\nTell the interface name for which you want to change the MAC Address :")
        new_mac = input("Provide a new MAC address for " + interface + ": ")
        option = (interface,new_mac)
        return option

    def change_mac(interface, new_mac):

        """Changing the mac address of the specified interface"""

        print("Changing mac address for " + interface + " to " + new_mac)
        subprocess.call(["ifconfig" , interface , "down"])
        subprocess.call(["ifconfig" , interface , "hw" , "ether" , new_mac])
        subprocess.call(["ifconfig" , interface , "up"])

    def get_current_mac(interface):

        """Getting the current mac of the interface"""

        ifconfig_result = str(subprocess.check_output(["ifconfig", options[0]]))
        mac_search_result  = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w" , ifconfig_result)

        if mac_search_result:
            return mac_search_result.group(0)

        else:
            print("Could not read the mac address..")

    options = get_arguments()
    current_mac = get_current_mac(options[0])

    print("Current mac = " + str(current_mac))
    change_mac(options[0] , options[1])

    current_mac = get_current_mac(options[0])

    if current_mac == options[1]:
        print("MAC Address changed successfully...")
    else:
        print("MAC address was not changed...")
