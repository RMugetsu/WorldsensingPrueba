import socket
import Funciones

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print(f"Se ha conectado correctamente!")
	clientsocket.send(bytes("Hola", "utf-8"))
	msg = clientsocket.recv(1024)
	Funciones.escribirRegistroDeLaTemperatura(msg.decode())
	clientsocket.close()


