import socket
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

# Basic user interface header
print(r"""
  _____   _____  _______  ______   _____  _    _   _____       _______  _____  _      
 |  __ \ |_   _||__   __||  ____| / ____|| |  | | |  __ \  /\ |__   __||_   _|| |     
 | |__) |  | |     | |   | |__   | (___  | |__| | | |__) |/  \   | |     | |  | |     
 |  _  /   | |     | |   |  __|   \___ \ |  __  | |  ___// /\ \  | |     | |  | |     
 | | \ \  _| |_    | |   | |____  ____) || |  | | | |   / ____ \ | |    _| |_ | |____ 
 |_|  \_\|_____|   |_|   |______||_____/ |_|  |_| |_|  /_/    \_\|_|   |_____||______|                                                                                                                                                                           
""")
print("\n****************************************************************")
print("\n* Copyright of Ritesh Patil, 2025                              *")
print("\n* https://github.com/Ritesh4501                                *")
print("\n* www.linkedin.com/in/riteshpatil16                            *")
print("\n****************************************************************")

open_ports = []
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        print("You entered a valid ip address.")
        break
    except:
        print("You entered an invalid ip address")
    

while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

# Basic socket port scanning
for port in range(port_min, port_max + 1):
    # Connect to socket of target machine. We need the ip address and the port number we want to connect to.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:
        pass

# We only care about the open ports.
for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")