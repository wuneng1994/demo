from socket import *
ip_port =("127.0.0.1",8000)
buffersize =1024
udp_client = socket(AF_INET,SOCK_DGRAM)
while True:
    msg = input(">>:").encode("utf-8")
    udp_client.sendto(msg,ip_port)
    data,addr = udp_client.recvfrom(buffersize)
    print(data.decode("utf-8"))

udp_client.close()