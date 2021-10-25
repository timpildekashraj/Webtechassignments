import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
req_u = s.recv(1024)

url = input(str(req_u.decode("utf-8")))
s.send(bytes(url,"utf-8"))
rep = s.recv(1024)

print(rep.decode("utf-8"))
