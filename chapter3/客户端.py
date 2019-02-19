from socket import *
ip_port = ("127.0.0.1",8000)
buffersize = 1024
tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)
print("双向链接建立成功")
while True:
    msg=input("》：").encode("utf-8")
    tcp_client.send(msg)
    data = tcp_client.recv(buffersize)
    print('接受到来自客户端的消息',data.decode("utf-8"))
conn.close()
tcp_client.close()
print('通讯结束')