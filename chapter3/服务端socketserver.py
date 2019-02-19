import socketserver
import struct
import subprocess

buffersize = 1024

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print(self.client_address)

        while True:
            try:
                cmd = self.request.recv(buffersize)
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
                self.request.send(msg_len)
                self.request.send(r.encode('utf-8'))
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(("127.0.0.1",8000),MyServer)
    s.serve_forever()