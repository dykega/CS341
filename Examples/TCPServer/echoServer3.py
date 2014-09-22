# Echo server program
import socket
import time

HOST = ''                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
QUEUELEN = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(QUEUELEN)

print("program started")
conn, addr = s.accept()  # blocks here
print("Connected to by",addr)
data = conn.recv(1024)
numData = data.decode('utf8')
numData = int(numData)

msg = str(numData)
conn.send(msg.encode('utf8'))

dataLst = [None] * numData
for num in range(numData):
    dataLst[num] = conn.recv(1024)

for data in dataLst:
    intData = data.decode('utf8')
    intData = int(data)
    intData = intData ** 2
    strData = str(intData)
    time.sleep(.1)
    conn.send(strData.encode('utf8'))
    
conn.close()
