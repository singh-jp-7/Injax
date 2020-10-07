#!/usr/bin/python3

import subprocess
import re
import optparse

def macchanger():

    def get_arguments():

        """"Getting the interface name and the new mac address"""
        
        # parser = optparse.OptionParser()
        # parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC Address of")
        # parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
        # (options, arguments) = parser.parse_args()
        # if not options.interface:
        #     parser.error("Please specify an interface or use --help for more info.")
        # elif not options.new_mac:
        #     parser.error("Please specify a new mac address or use -- help for more info.")
        # return options
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
