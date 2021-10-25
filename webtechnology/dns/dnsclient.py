import socket

host = socket.gethostname()
ipaddr = "127.0.0.1"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = (ipaddr, 1234)

choice = "Y"
while choice.upper() == "Y":
    req_domain = input("Enter domain name for which the ip is needed:")
    send = s.sendto(req_domain.encode(), addr)
    data, address = s.recvfrom(1024)
    reply_ip = data.decode().strip()
    print(f"The ip for the domain name {req_domain} : {reply_ip}")
    choice = input("Continue? (y/n)")
s.close()

