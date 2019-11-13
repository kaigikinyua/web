import socket
class Network:
	def getIp(self):
		try:
			import netifaces
			ip=netifaces.ifaddresses('wlo1')[netifaces.AF_INET][0]['addr']
			print(ip)
			if(ip=='127.0.0.1'):
				print("You are offline")
			Ip=ip+":4000"
			return Ip
		except:
			return "offline"