from socket import *
import struct
ip_port =("127.0.0.1",8000)
buffersize =1024
tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input(">>:")
    if not cmd:continue
    tcp_client.send(cmd.encode("utf-8"))
    len_msg =struct.unpack('i',tcp_client.recv(4))[0]
    data = b""
    print(len_msg)
    while len(data) < len_msg:
        print(len(data))
        data = data + tcp_client.recv(buffersize)
        
    print('end')
    print(data.decode("utf-8"))



tcp_client.close()