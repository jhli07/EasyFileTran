import  struct
import subprocess

def ssh(conn,cmd):
    cmds=cmd[0]
    obj = subprocess.Popen(cmds, shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    stdout = obj.stdout.read()
    stderr = obj.stderr.read()
    totle=(len(stdout)+len(stderr))
    conn.send(struct.pack('i',totle))
    conn.send(stdout)
    conn.send(stderr)