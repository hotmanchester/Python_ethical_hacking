import scapy.all as scapy
import argparse
def get_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target',dest='target',help='Target IP / IP range')
    options = parser.parse_args()
    if not options.target:
        print('[-] Please specify the network address')
        exit()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst ='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request # create new packet combining previous two
    answered_list = scapy.srp(arp_request_broadcast, timeout=1 , verbose=False)[0] #srp send packet and receives the response
    clients_list=[]
    for element in answered_list:
        client_dict = {"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------------------")
    for client in result_list:
        print(client["ip"]+"\t\t"+client["mac"])

options = get_arg()
scan_result = scan(options.target)
print_result(scan_result)
