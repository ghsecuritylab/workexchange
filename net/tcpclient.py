import socket
target_host = "0.0.0.0"
target_port = 2002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send("Hello")
response = client.recv(4096)
print response
