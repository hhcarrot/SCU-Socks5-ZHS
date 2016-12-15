from socket import *
from select import select
import threading

buffersize = 5900
authentication = True
VER = 0x05

def startclient(clientsocket, clientaddress):
    transpondsocket = socket(AF_INET, SOCK_STREAM)
    transpondsocket.connect(("47.89.194.114", 8900))

    if authentication:
        receivebuffer = clientsocket.recv(buffersize)
        transpondsocket.send((chr(VER) + chr(0x01) + chr(0x02)).encode()[::-1])
        receivebuffer = (transpondsocket.recv(buffersize))
        transpondsocket.send((chr(0x01) + chr(len(username)) + username + chr(len(password)) + password).encode()[::-1])
        receivebuffer = (transpondsocket.recv(buffersize))
        clientsocket.send(receivebuffer)

    socks = []
    socks.append(clientsocket)
    socks.append(transpondsocket)
    while True:
        r, w, e = select(socks,[],[])
        for i in r:
            if i is clientsocket:
                receivebuffer = clientsocket.recv(buffersize)
#                print("client: ", receivebuffer)
                reversebuffer = receivebuffer[::-1]
#                print("clientreverse: ", reversebuffer)
                if len(receivebuffer) > 0:
                    transpondsocket.send(reversebuffer)
                else:
                    for j in socks:
                        j.close()
                    return
            elif i is transpondsocket:
                receivebuffer = (transpondsocket.recv(buffersize))
#                reversebuffer = receivebuffer[::-1]
#                print("server: ", reversebuffer)
                if len(receivebuffer) > 0:
                    clientsocket.send(receivebuffer)
                else:
                    for j in socks:
                        j.close()
                    return

print("Starting...")
address = input("Please input client address:")
port = int(input("Please input client port:"))

if authentication:
    username = input("Please input username:")
    password = input("Please input password:")

listensocket = socket(AF_INET, SOCK_STREAM)
listensocket.bind((address, port))
listensocket.listen(9)
while True:
    clientsocket, clientaddress = listensocket.accept()
    childthread = threading.Thread(target = startclient, args = (clientsocket, clientaddress))
    childthread.start()
