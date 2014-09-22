# Echo client program
import socket

HOST = '172.24.13.177'    # The remote host
PORT = 50007              # The same port as used by the server

print("Enter numbers line by line and enter stop to finish")
estring = ""
nums = []
while estring != "stop":
    estring = input("-> ")
    if estring != "stop":
        nums.append(estring)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
lenStr = str(len(nums))
s.send(lenStr.encode('utf8'))

data = s.recv(1024)
numReturn = data.decode('utf8')
numReturn = int(numReturn)

for num in nums:
    numStr = str(num)
    s.send(numStr.encode('utf8'))

for num in range(numReturn):
    data = s.recv(1024)
    sqrNum = data.decode('utf8')
    print(sqrNum)  

s.close()
