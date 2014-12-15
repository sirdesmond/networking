import socket
import time

def main():
	host = '127.0.0.1'
	port = 5001

	server = ('127.0.0.1',5000)

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	s.bind((host,port))

	print 'Enter q or quit to exit'
	message = raw_input("->")

	while message not in ('q','quit'):
		print 'Sending...'
		s.sendto(message,server)
		time.sleep(3)
		data,addr = s.recvfrom(1024)

		print 'Received from server: ', str(data)

		message = raw_input('->')

	s.close()

if __name__ == '__main__':
	main()
