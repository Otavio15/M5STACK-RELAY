
import socket

serverHost = '192.168.0.104'
serverPort = 50007

mensagem = [b'b']

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect((serverHost, serverPort))

for linha in mensagem:
  sockobj.send(linha)

  data = sockobj.recv(1024)
  print('Cliente recebeu: ', data)

sockobj.close

