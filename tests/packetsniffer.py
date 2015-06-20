import socket
import struct


HOST = input('What is your IP Address')
# host to listen

def sniffing(host, win, socket_prot):
    while 1:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_prot)
        sniffer.bind((host, 0))
        # include the IP headers in the captured packets
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        raw_buffer = sniffer.recvfrom(65565)[0]
        ip_header = raw_buffer[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        # Create our IP structure
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);

        print('IP -> Version:' + str(version) + ', Header Length:' + str(ihl) + ', TTL:' + str(ttl) + ', Protocol:' + str(protocol) + ', Source:' + str(s_addr) + ', Destination:' + str(d_addr))

def main(host):
    sniffing(host, 1, socket.IPPROTO_IP)

if __name__ == '__main__':
    main(HOST)