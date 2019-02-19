from socket import *

ip_port =("127.0.0.1",8000)
backlog = 5
buffersize =1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.bind(ip_port)
tcp_client.listen(backlog)
while True:
    conn,addr = tcp_client.accept()
    print('链接建立成功:',addr)
    conn.send(b"123")
    conn.send(b"456")
    conn.close()
tcp_client.close()
