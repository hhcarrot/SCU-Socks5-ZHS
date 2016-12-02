# This is a socks5 server

buffersize = 5900
authentication = False
VER = 0x05

from socket import *
from select import select
import threading

def startserver(address, port):
    listensocket = socket(AF_INET, SOCK_STREAM)
    listensocket.bind((address, port))
    listensocket.listen(9)
    print("server listening ...")

    while True:
        connectsocket, clientaddress = listensocket.accept()
        print("client connecting...")
        childthread = threading.Thread(target = startsocks5, args = (connectsocket, clientaddress))
        #childthread = threading.Thread(target=startsocks5, args=(connectsocket, clientaddress))
        childthread.start()

def startsocks5(connectsocket, clientaddress):

    receivebuffer = (connectsocket.recv(buffersize))[::-1]
    print(receivebuffer)
    if len(receivebuffer) == 0:
        print("client quit...")
        connectsocket.close()
        return
    print("VER: ", ord(receivebuffer[0:1]))
    if ord(receivebuffer[0:1]) == VER:
        #print("socks5")
        NMETHODS = ord(receivebuffer[1:2])
        METHODS = []
#        for i in receivebuffer[2:]:
#            METHODS.append(ord(i))
        if authentication:
            pass
        else:
            METHOD = 0x00
            connectsocket.send((chr(VER) + chr(METHOD)).encode())


    receivebuffer = (connectsocket.recv(buffersize))[::-1]
    print(receivebuffer)
    if len(receivebuffer) == 0:
        print("client quit...")
        connectsocket.close()
        return
    print("VER: ", ord(receivebuffer[0:1]), "| CMD: ", ord(receivebuffer[1:2]), "| ATYP: ", ord(receivebuffer[3:4]))
    CMD = ord(receivebuffer[1:2])
    ATYP = ord(receivebuffer[3:4])
    if CMD == 0x01:
        if ATYP == 0x03:
            DSTADDRLEN = ord(receivebuffer[4:5])
            DSTADDR = gethostbyname(receivebuffer[5:5 + DSTADDRLEN])
            DSTPORT = ord(receivebuffer[5 + DSTADDRLEN:5 + DSTADDRLEN + 1]) * 256 + ord(receivebuffer[5 + DSTADDRLEN + 1:5 + DSTADDRLEN + 2])


    connectsocket.send((chr(VER) + "\x00\x00\x01\x00\x00\x00\x00\x00\x00").encode())
    transpond(connectsocket, DSTADDR, DSTPORT)

def transpond(connectsocket, DSTADDR, DSTPORT):
    transpondsocket = socket(AF_INET, SOCK_STREAM)
    transpondsocket.connect((DSTADDR, DSTPORT))

    socks = []
    socks.append(connectsocket)
    socks.append(transpondsocket)
    while True:
        r, w, e = select(socks,[],[])
        for i in r:
            if i is connectsocket:
                receivebuffer = (connectsocket.recv(buffersize))[::-1]
                if len(receivebuffer) > 0:
                    transpondsocket.send(receivebuffer)
                else:
                    for j in socks:
                        j.close()
                    return
            elif i is transpondsocket:
                receivebuffer = transpondsocket.recv(buffersize)
                if len(receivebuffer) > 0:
                    connectsocket.send(receivebuffer)
                else:
                    for j in socks:
                        j.close()
                    return


#        else:
#            print(clientaddress, receivebuffer)

#def startsocks5(connectsocket, clientaddress):
#    receivebuffer = (connectsocket.recv(buffersize)).decode()


print("Starting...")
address = input("Please input server address:")
port = int(input("Please input server port:"))
startserver(address, port)
