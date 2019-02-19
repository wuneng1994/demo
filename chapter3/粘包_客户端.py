from socket import *
import time
ip_port =("127.0.0.1",8000)
backlog = 5
buffersize =1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
time.sleep(0.5)
print('与服务器链接建立成功')
data = tcp_client.recv(buffersize)
print(data.decode("utf-8"))
tcp_client.close()
