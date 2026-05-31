import struct

def get_ssh(client,cmds):
    recv_sizessh=0
    recv_data=b''
    total = client.recv(4)
    total_sizessh=struct.unpack('i',total)[0]
    while (recv_sizessh < total_sizessh):
        line = client.recv(1024)
        recv_size=len(line)
        recv_sizessh += recv_size
        recv_data += line
    print(recv_data.decode('GBK'))