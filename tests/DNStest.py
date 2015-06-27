__author__ = 'julia'

import socket
from tests.Test import Test


class DNStest(Test):
    def __init__(self, name, DNS_name, expected_ip_address_list):
        super(DNStest, self).__init__(name)
        self.ip_list = []
        self.expected_ip_address_list = expected_ip_address_list
        self.DNS_name = DNS_name
    def run(self):
        get_ip_from_dns = socket.getaddrinfo(self.DNS_name,0,0,0,0)
        for result in get_ip_from_dns:
            self.ip_list.append(result[-1][0])

        if self.ip_list == self.expected_ip_address_list:
            return True
        else:
            return False

instance_DNS = DNStest('NSlookup check', 'www.dropbox.com', ['108.160.172.206', '108.160.172.238'])
print (instance_DNS.get_name())
print(instance_DNS.run())
