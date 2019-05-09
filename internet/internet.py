import socket

ip = '10.153.119.254'
port = 12345

string  = "Hello World\nThanks for visiting"


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname(socket.gethostname()))
s.bind((socket.gethostname(), port))
s.listen(5)

while True:
    client, addr = s.accept()
    client.sendall(bytes(string, "utf-8"))
    client.close()
    
