import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.30'          # Enter the IP of the workstation here
port = 80                      # Select port which should be connected

try:
    s.connect((host, port))    # tries to connect to the host
    exit(1)                    # return 1 - successful
except socket.error as e:      # if failed to connect
#   print(e)                   # socket error message turned off
    exit(0)                    # return 0 - unsuccessful

s.close()                      # close socket
