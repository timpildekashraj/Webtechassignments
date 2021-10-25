import socket

dns_table = {"www.google.com":"142.250.183.228",
             "www.hackerone.com":"104.16.99.52",
             "www.portswigger.net":"34.255.175.180",
             "www.youtube.com":"142.250.67.46"}
             
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Starting Server...")
s.bind(("127.0.0.1",1234))

while True:
    data, address = s.recvfrom(1024)
    print(f"{address} wants to fetch data!")
    data = data.decode()
    ip = dns_table.get(data, "Not Found!").encode()
    send = s.sendto(ip,address)
s.close()
