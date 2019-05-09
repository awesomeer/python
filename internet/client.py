import socket

port = int(input("Enter port to connect to: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))
send = bytes(input("Enter some text: "), "utf-8")
s.send(send)
back = "Server sent back: "
print(back + s.recv(1024).decode("utf-8"))
