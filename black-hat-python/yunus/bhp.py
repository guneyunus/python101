import socket

target_host = "0.0.0.0"
target_port = 9998

#create a socket object
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connet the client 
client.connect((target_host,target_port))

client.send(b"GET / HTTPS/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()