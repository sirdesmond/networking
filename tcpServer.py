import socket
import time

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()

	s.bind((host,port))

	s.listen(1)

	conn, addr = s.accept()

	print "Connection established with " + str(addr)

	while True:
		data = conn.recv(1024)

		if not data:
			break
		print "from connected user: " + str(data)

		data = str(data).upper()

		print "sending", str(data)
		time.sleep(3)
		conn.send(data)

	conn.close()

if __name__ == '__main__':
	main()
