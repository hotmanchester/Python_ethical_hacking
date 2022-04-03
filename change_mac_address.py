#!/usr/bin/env python3
import subprocess
import re
import argparse




def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface")
    parser.add_argument("-m", "--mac", dest="mac")
    options = parser.parse_args()
    # print(options.interface)
    # print(options.mac)
    if not options.interface:
        parser.error("[-] Please specify an interface")
    elif not options.mac:
        parser.error("[-] Please specify a new mac")
    return options

def change_mac(interface,mac):
    print("[+] Changing MAC address for " + interface + " to " + mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])




def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
    mac_address_search_result = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC.")
        #exit()


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC: " + str(current_mac))
change_mac(options.interface,options.mac)
new_mac = get_current_mac(options.interface)
print("New MAC address: "+ new_mac)




