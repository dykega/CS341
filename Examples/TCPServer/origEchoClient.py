# Echo client program
import socket
import time

HOST = '192.203.196.71'    # The remote host
PORT = 8002            # The same port as used by the server

estring = "Chelsea FC"
startTime = time.time()
trials = 50

for num in range(trials):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(estring.encode('utf8'))  # encode needed in Python3
    data = s.recv(1024)
    s.close()

endTime = time.time()
print("Total time was:",str(endTime-startTime)[:6],"seconds.")
print("Able to send", str(trials/(endTime-startTime))[:6],"messages per second.")