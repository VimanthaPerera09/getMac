from getmac import get_mac_address
import sys

def getMac(IP):
    mac = get_mac_address(ip=IP)
    print(mac)

mac_add=sys.argv[1]

getMac(mac_add)