import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	client, addr = s.accept()
	print(addr)
	client.send(b'Hello World')
	client.close()