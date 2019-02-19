from socket import *
ip_port =("127.0.0.1",8000)
buffersize =1024
udp_client = socket(AF_INET,SOCK_DGRAM)
udp_client.bind(ip_port)
while True:
    data,addr = udp_client.recvfrom(buffersize)
    print(data.decode("utf-8"))
    udp_client.sendto(data.upper(),addr)

udp_client.close()