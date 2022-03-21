# Importar o modulo socket

import socket


HOST = 'localhost'
PORT = 50000

s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print('AGUARDANDO')
conn,ender = s.accept()#metodo para aceitar a conexao

print('Conetado em ',ender)

while True:
    data = conn.recv(1024)
    data_upper = data.upper()

    """if not data:
        print('Fechando a Connexao')
        conn.close()
        break"""
        
    conn.sendall(data_upper)
    
