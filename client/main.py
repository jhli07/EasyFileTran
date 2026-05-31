import socket
import struct
from get_file import get_file
from put_file import put_file
from ssh import get_ssh

def main():

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        obj_ip=input('请输入目标主机ip地址：')
        obj_port = int(input('请输入目标主机端口：'))

        client.connect((obj_ip,obj_port))
        print('连接成功!')

        while True:
            cmd=input(obj_ip+":>> ").strip()
            if not cmd:continue
            client.send(cmd.encode('utf-8'))

            cmds = cmd.split()
            if(cmds[0]=='get'):
                get_file(client,cmds)


            elif(cmds[0]=='put'):
                put_file(client,cmds)

            else:
                get_ssh(client,cmds)


        client.close()





