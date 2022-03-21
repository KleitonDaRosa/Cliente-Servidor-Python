import socket

HOST = 'localhost'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
nome=input('Qual o seu nome? ')
s.sendall(str.encode(nome))
data = s.recv(1024)




print('MEnsagem Ecoada>',data.decode())
