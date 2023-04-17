#!/usr/bin/python3

# By 4ndyMcFly

from tqdm import tqdm
from time import sleep
from colorama import init, Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor, as_completed

import socket, os, sys

def scan(ip, p1, p2):
    if p1 <= p2:
        os.system ("clear")
        print(Fore.BLACK+Back.YELLOW + "\n[+]--- MULTI-THREAD PYTHON PORTSCAN ---[+]"+ Fore.RESET + Back.RESET + "\n\nBy: 4ndymcfly\n")
        print("\nTarget IP: " + Style.BRIGHT + str(ip) + Style.RESET_ALL)
        print("Scanning ports from " + str(port1) + " to " + str(port2) + "...\n" + Fore.GREEN)

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(scan_ports, ip, i) for i in range(p1,p2+1)]
            for f in tqdm(as_completed(futures), total=len(futures), desc="Progress"):
                pass

        print(Fore.RESET + "\n\nPorts open = " + Fore.YELLOW + str(listopen) + "\n\n\n" + Fore.RESET)
    else:
        print("\nERROR: Port range is wrong.")

def scan_ports(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    result = s.connect_ex((ip, int(port)))

    if result == 0:
        listopen.append(port)
    else:
        listclosed.append(port)

if len(sys.argv) == 4:
    ip = sys.argv[1]
    port1 = int(sys.argv[2])
    port2 = int(sys.argv[3])
    listopen = []
    listclosed =[]

    scan(ip, port1, port2)

else:
    print("Error: Enter parameters correctly.")
    print("Example: \"192.168.1.1 22 80\"")
