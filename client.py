import socket
import Funciones

temperatura = Funciones.obtenerTemperaturaCPU()
#AF_INET Corresponde a IPv4
#SOCK_STREAM Corresponde al protocolo TCP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = s.recv(1024)
print(msg.decode())
s.send(bytes(str(temperatura), "utf-8"))