import socket
n = 0
while n != 3:

	print("\n Menu: \n 1. DNS 2. Reverse DNS 3. Exit \n")
	n = int(input("\n ENter your choice"))
	
	if n== 1:
		print('Welcome to DNS to IP Adress')
		URL = input('Enter URL: ')
		addr1 = socket.gethostbyname(URL)
		print(addr1)
	elif n == 2:
		print('Welcome IP address to DNS')
		IP = input('Enter IP adress: ')
		addr6 = socket.gethostbyaddr(IP)
		print(addr6)
