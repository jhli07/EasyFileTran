import socket
import subprocess
import json
import struct
from put_file import put_file
from get_file import get_file
from ssh import ssh

def main():

    port = int(input('输入你要开启的端口：'))
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('0.0.0.0',port))
    server.listen(5)

    print('正在等待客户端连接......')

    while True:
        conn, client_addr = server.accept()
        print('客户端已连接!')

        while True:
            try:
                res = conn.recv(8096)
                if not res: break
                cmd = res.decode('utf-8').split()
                if(cmd[0]=='get'):
                    put_file(conn,cmd)

                elif(cmd[0]=='put'):
                    get_file(conn,cmd)

                else:
                    ssh(conn, cmd)


            except ConnectionResetError:
                break



        conn.close()


    server.close()