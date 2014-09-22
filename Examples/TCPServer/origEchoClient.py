# Echo client program
import socket
import time

HOST = '10.24.46.224'    # The remote host
PORT = 50008              # The same port as used by the server

estring = "Chelsea FC"
startTime = time.time()

for num in range(50):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(estring.encode('utf8'))  # encode needed in Python3
    data = s.recv(1024)
    s.close()

endTime = time.time()
print(endTime-startTime, (endTime-startTime)/50 )