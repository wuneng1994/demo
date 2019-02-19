from socket import *
ip_port = ("127.0.0.1",8000)
backlog = 5
buffersize = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_client.bind(ip_port)
tcp_client.listen(backlog)
while True:
    print("服务器开始运行")
    conn,addr = tcp_client.accept()#服务器阻塞
    print("双向链接为",conn)
    print("客户端地址为",addr)

    while True:
        # try:
        data = conn.recv(buffersize)
        if not data:break
        print('接受到来自客户端的消息',data.decode("utf-8"))
        conn.send(data.upper())
        # except Exception:
            # break
    conn.close()
tcp_client.close()
print('通讯结束')