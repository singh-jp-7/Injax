#!/usr/bin/python3
import scapy.all as scapy
from mac_vendor_lookup import MacLookup

def net_scan():
    try:
        ip1 = input("Enter the ip address you want to scan for : ")
        rng = input("Enter the CIDR(Eg:8,16,24): ")
        ip = ip1 + "/" + rng

        def scan(ip):
            arp_request = scapy.ARP(pdst=ip)
            broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast/arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
            clients_list = []
            for element in answered_list:
                client_dict = {"ip" : element[1].psrc, "mac": element[1].hwsrc ,"vendor": MacLookup().lookup(element[1].hwsrc)}
                clients_list.append(client_dict)
            return clients_list

        def print_results(results_list):
            print("IP\t\t\tMAC Address\t\t\t\tMAC Vendor \n\n---------------------------------------------------------------------------------\n\n")
            for client in results_list:
                print(client["ip"] + "\t\t" + client["mac"] + "\t\t\t"+ client["vendor"] )


        scan_result = scan(ip)
        print_results(scan_result)
    except KeyboardInterrupt:
    print("\n[+]Detected Ctrl + C exiting...")
