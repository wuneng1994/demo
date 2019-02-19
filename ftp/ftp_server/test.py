with open(r"D:\XMind\图片1.png",'rb') as f:
    data = f.read()

with open(r"d:/1.png",'wb+') as f:
    f.write(data)    

seek #控制文件指针位置
"ab+" #二进制追加模式写文件