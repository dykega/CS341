# Echo server program
import socket
import time

def toByteArr(lst):
    bytArr = bytearray([])
    lenInt = len(lst)

    bytArr.append(lenInt >> 24)
    bytArr.append(lenInt >> 16 & 0xff)
    bytArr.append(lenInt >> 8 & 0xff)
    bytArr.append(lenInt & 0xff)

    for num in lst:
        bytArr.append(num >> 24)
        bytArr.append(num >> 16 & 0xff)
        bytArr.append(num >> 8 & 0xff)
        bytArr.append(num & 0xff)

    return bytArr

def toInts(bytArr):
    lst = []
    lenNum = 0x00

    lenNum = lenNum | bytArr[0]
    lenNum = lenNum << 8
    lenNum = lenNum | bytArr[1]
    lenNum = lenNum << 8
    lenNum = lenNum | bytArr[2]
    lenNum = lenNum << 8
    lenNum = lenNum | bytArr[3]
    

    for pos in range(4,4+(lenNum*4),4):
        num = 0x00
        num = num | bytArr[pos]
        num = num << 8
        num = num | bytArr[pos+1]
        num = num << 8
        num = num | bytArr[pos+2]
        num = num << 8
        num = num | bytArr[pos+3]
        lst.append(num)

    return lst


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

dataNums = toInts(data)
for pos in range(len(dataNums)):
    dataNums[pos] = dataNums[pos] ** 2

sqrNums = toByteArr(dataNums)
conn.send(sqrNums)
    
conn.close()
