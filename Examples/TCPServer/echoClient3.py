# Echo client program
import socket

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


HOST = '10.24.44.181'# address of remote host
PORT = 50007              # The same port as used by the server

print("Enter numbers line by line and enter stop to finish")
estring = ""
nums = []
while estring != "stop":
    estring = input("-> ")
    if estring != "stop":
        nums.append(int(estring))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(toByteArr(nums))
sqrNums = s.recv(1024)
sqrNums = toInts(sqrNums)
print(sqrNums)

s.close()
