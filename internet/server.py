import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("listening on port " + str(port))
for i in range(5):
	client, addr = s.accept()
	print(addr)
	client.send(client.recv(1024))
	client.close()

s.close()
