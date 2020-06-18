import socket
f = open("demofile.txt", "w")

#define 
HOST = 'riweb.tibeica.com'
PORT = 80

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket = (HOST, PORT)
clientSocket.connect(serverSocket)
user = "name"
req = b'GET /crawl/ HTTP/1.1\r\nHost: riweb.tibeica.com\r\nUser-agent: xd\r\nConnection: close\r\n\r\n'
clientSocket.sendall(req)

resp = ''
while True:
    recv = clientSocket.recv(1024)
    if not recv:
        break
    resp +=str(recv)

print(resp)
clientSocket.close()
