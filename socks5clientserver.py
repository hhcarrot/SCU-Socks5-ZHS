from socket import *
from select import select
import threading
#import GUI

buffersize = 5900
authentication = True
VER = 0x05
#dstaddress = ""
#dstport = 0
listensocket = socket(AF_INET, SOCK_STREAM)
blockurl = []
blockip = []

def startclient(clientsocket, clientaddress, dstaddress, dstport, username, password):
    transpondsocket = socket(AF_INET, SOCK_STREAM)
    #print(dstaddress, dstport)
    transpondsocket.connect((dstaddress, dstport))

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
                if (receivebuffer[0:3].decode()) == ('GET'):
                    m = receivebuffer.decode().split(' ')[0]
                    src = receivebuffer.decode().split(' ')[1]
                    test = receivebuffer.decode().split(' ')[2]
                    test2 = receivebuffer.decode().split(' ')[3]
                    #print(m)
                    #print(src)
                    #print(test)
                    #print(test2.replace("\r\n", "").replace("User-Agent:", ''))
                    urlget = test2.replace("\r\n", "").replace("User-Agent:", '') + src
                    ipget = gethostbyname(test2.replace("\r\n", "").replace("User-Agent:", ''))
                    if urlget in blockurl:
                        for j in socks:
                            print("blocked url:", urlget)
                            j.close()
                            return
                    if ipget in blockip:
                        for j in socks:
                            print("blocked ip:", ipget)
                            j.close()
                            return
                    #print("url:"+test2.replace("\r\n", "").replace("User-Agent:", '') + src)
                    print(urlget)
                    print(ipget)
                    #print(receivebuffer)
#                print("client: ", receivebuffer)
                reversebuffer = receivebuffer[::-1]
#                print("clientreverse: ", reversebuffer)
                if len(receivebuffer) > 0:
                    if authentication:
                        transpondsocket.send(reversebuffer)
                    else:
                        transpondsocket.send(receivebuffer)
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


def startengine(resUsername, resPassword, resAddress, resPort):

    file = open('blockurl.txt')

    while True:
        line = file.readline()
        if not line:
            break
        blockurl.append(line)

    file.close()

    file = open('blockip.txt')

    while True:
        line = file.readline()
        if not line:
            break
        blockip.append(line)

    file.close()


    print("Starting...")
    #address = input("Please input client address:")
    address = 'localhost'
    #port = int(input("Please input client port:"))
    port = 8900

    if authentication:
        #username = input("Please input username:")
        username = resUsername
        print('username: ' + username)
        #password = input("Please input password:")
        password = resPassword
        print('username' + password)
    else:
        username = ""
        password = 0

    dstaddress = resAddress
    print("serveraddress: ", dstaddress)
    dstport = int(resPort)
    print("serverport: ", dstport)

    #listensocket.close()
    #listensocket = socket(AF_INET, SOCK_STREAM)
    global listensocket
    listensocket.close()
    listensocket = socket(AF_INET, SOCK_STREAM)
    listensocket.bind((address, port))
    listensocket.listen(9)
    while True:
        clientsocket, clientaddress = listensocket.accept()
        childthread = threading.Thread(target = startclient, args = (clientsocket, clientaddress, dstaddress, dstport, username, password))
        childthread.start()
