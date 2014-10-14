# unreliable data transfer functions
# You may not modify either udt_send or udt_recv

from udt import *
import socket

# example of use with echoServer
if __name__ == '__main__':
    estring = ""
    seqNum = 0
    while estring.lower() != "exit":
        done = False
        print("Enter a message")
        estring = input("-> ")
        while not done: 
            pkt = make_pkt(estring,seqNum,'localhost',51423)
            sock = udt_send(pkt)
            pkt,addr = udt_recv(sock)
            if pkt and not pkt.is_corrupt and pkt.seqnum == seqNum:
                print(pkt.mess)
                print()
                done = True
            elif pkt and pkt.is_corrupt:
                print("received corrupt packet. Resending")
            elif pkt and pkt.seqnum != seqNum:
                print("recevied wrong sequence num (sent corrupt). Resending")

        if seqNum == 0:
            seqNum = 1
        else:
            seqNum = 0


