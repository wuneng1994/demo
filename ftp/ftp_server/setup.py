#命令处理模块
'''
cd path 切换
del filename 删除
move filename1 filename2 移动文件1位置到2位置
get filename filepath 下载文件至filepath
upload filename filepath 上传文件至filepath
signin username password 登录
dir 查看当前目录下的文件和文件夹子
pwd 获得当前目录
'''
def deal_cd(cmd):
    global cwd="c:"  #设置工作目录
    return real_cmd #返回客户端真实执行的命令
