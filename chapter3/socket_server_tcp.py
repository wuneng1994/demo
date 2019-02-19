from socket import *
import subprocess
import struct
import os

ip_port =("127.0.0.1",8000)
backlog = 5
buffersize =1024

tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(ip_port)
tcp_server.listen(backlog)

while True:
    conn,addr = tcp_server.accept()
    print("接受到新的链接",addr)
    try:
        while True:
            cmd = conn.recv(buffersize)
            print(cmd.decode("utf-8"))
            res = subprocess.Popen(cmd.decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                res_msg = err
            else:
                res_msg = res.stdout.read()
                if not res_msg:
                    res_msg = ("CMD %s 执行成功!" % cmd.decode("utf-8") ).encode("gbk")
                
            r=res_msg.decode("gbk")
            print(r)
            print(len(res_msg))
            msg_len = struct.pack("i",len(res_msg))
            conn.send(msg_len)
            conn.send(r.encode('utf-8'))
    except:
        pass


    conn.close()

