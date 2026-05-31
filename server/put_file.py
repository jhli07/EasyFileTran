import os
import json
import struct

share_dir=r'EasyFileTran\server\share'

def put_file(conn, cmd):

       try:
            filename = cmd[1]
            header_dic = {
                'filename': filename,
                'file_size': os.path.getsize(r'%s/%s' % (share_dir, filename))
            }
            header_json = json.dumps(header_dic)

            header_bytes = header_json.encode('utf-8')

            conn.send(struct.pack('i', len(header_bytes)))

            conn.send(header_bytes)

            with open('%s/%s' % (share_dir, filename), 'rb') as f:
                for line in f:
                    conn.send(line)

       except FileNotFoundError:
          print('系统找不到对应文件')

