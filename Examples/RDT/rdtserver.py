import socket, traceback
from udt import *

host = ''                               # Bind to all interfaces
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
seqNum = 0

while True:
    try:
        pkt,address = udt_recv(s)
        if pkt and not pkt.is_corrupt and pkt.seqnum == seqNum:
            print("Got good data from", address, pkt.mess)
            pkt.mess = "ACK"
            pkt.seqnum = seqNum
            pkt.ip = address[0]
            pkt.port = address[1]
            pkt.is_corrupt = False
            udt_send(pkt)
            if seqNum == 0:
                seqNum = 1
            else:
                seqNum = 0
            print()
        elif pkt and pkt.is_corrupt:
            print("Received corrupt packet")
            pkt.mess = "ACK"
            if seqNum == 0:
                pkt.seqnum = 1
            else:
                pkt.seqnum = 0
            pkt.ip = address[0]
            pkt.port = address[1]
            pkt.is_corrupt = False
            udt_send(pkt)
        elif pkt == None:
            print("UDT timed out")

    except (KeyboardInterrupt, SystemExit):
        break
    except:
        traceback.print_exc()
