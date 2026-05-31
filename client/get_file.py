import  struct
import  json
download_dir=r'EasyFileTran\client\download'

def get_file(client,cmds):
    obj = client.recv(4)
    header_size = struct.unpack('i', obj)[0]

    header_bytes = client.recv(header_size)

    header_json = header_bytes.decode('utf-8')#完整的json数据
    header_dic = json.loads(header_json)
    total_size=header_dic['file_size']
    filename=header_dic['filename']

    with open('%s/%s' %(download_dir,filename),'wb') as f:
        recv_size=0
        while(recv_size < total_size):
            line=client.recv(1024)
            f.write(line)
            recv_size+=len(line)
            print('总大小%s  已下载%s' %(total_size,recv_size))