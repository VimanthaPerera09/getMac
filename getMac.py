import nmap
from getmac import get_mac_address

class Network(object):
    def __init__(self):
        ip = input('Please enter your ip address: ')
        self.ip = ip
    
    def getMac(self, IP='192.168.2.1'):
        mac = get_mac_address(ip=IP)
        print(mac)
        return mac

    
    def networkscanner(self):
    
        network = self.ip + '/24'

        print('Scanning........')

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host , status in hosts_list:
            mac=self.getMac(IP=host)
            print('Host\t{}'.format(host))

if __name__ == "__main__":
    D = Network()
    D.networkscanner()


