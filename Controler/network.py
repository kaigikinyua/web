import socket
class Network:
	def getIp(self):
		ip=socket.gethostbyname(socket.getfqdn())
		print(ip)
		if(ip=='127.0.0.1'):
			print("You are offline")
		return ip