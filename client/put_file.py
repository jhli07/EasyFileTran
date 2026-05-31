import struct
import json
import os
download_dir=r'\EasyFileTran\client\download'

def put_file(client,cmds):

   try:
        filename = cmds[1]
        header_dic = {
            'filename': filename,
            'file_size': os.path.getsize(r'%s/%s' %(download_dir,filename))
        }
        header_json = json.dumps(header_dic)

        header_bytes = header_json.encode('utf-8')

        client.send(struct.pack('i', len(header_bytes)))

        client.send(header_bytes)

        with open('%s/%s' %(download_dir,filename), 'rb') as f:
             send_size = 0
             for line in f:
                client.send(line)
                send_size+=len(line)
                print('总大小%s  已上传%s' % (header_dic['file_size'], send_size))
        print('上传成功！')


   except FileNotFoundError:
         print('系统找不到对应文件')