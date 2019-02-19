from socket import *
import time
ip_port =("127.0.0.1",8000)
buffersize =1024
udp_client = socket(AF_INET,SOCK_DGRAM)
#udp_client.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
udp_client.bind(ip_port)
while True:
    data,addr = udp_client.recvfrom(buffersize)
    if not data:
        fmt = "%Y-%m-%d %X"
    else:
        fmt = data.decode("utf-8")
    print(data.decode("utf-8"))
    stdtime = time.strftime(fmt).encode("utf-8")
    udp_client.sendto(stdtime,addr)

udp_client.close()