import mysql.connector
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Waiting for incoming connections...")

clientsocket, address = s.accept()
print(f"Connection from {address} has been established!")
clientsocket.send(bytes("Enter url: ","utf-8"))
url = clientsocket.recv(1024)
url=url.decode("utf-8")

myconn = mysql.connector.connect(host="localhost",user="root",passwd="Timpil17",database="dns1")
print("Database connection establised")
cur = myconn.cursor()
cur.execute("select count(ip_address) from dns_models1 where domain_name=\""+url+"\"")


for x in cur:
    count=x[0]
if(count>0):
    try:

        cur.execute("select ip_address from dns_models1 where domain_name=\""+url+"\"")
    except:
        myconn.rollback()
    for x in cur:
         clientsocket.send(bytes("ip-address: "+x[0],"utf-8"))

else:
    clientsocket.send(bytes("invalid url","utf-8"))
myconn.close()
