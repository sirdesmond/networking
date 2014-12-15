import socket
import time
def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()

	print 'Connnecting to server @ 127.0.0.1:5000'
	s.connect((host,port))
	time.sleep(5)

	print 'You can enter q or quit to exit!!'

	message = raw_input("->")

	while message not in ('q','quit'):
		s.send(message)
		data = s.recv(1024)

		print 'received from server: '+ str(data)

		message = raw_input("->")
	s.close()

if __name__ == '__main__':

	
	main()