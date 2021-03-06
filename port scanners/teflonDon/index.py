import optparse
from socket import *

def connScan(tgtHost, tgtPort):
	tgtPortS = int(tgtPort)
	try: 
		socket = socket(AF_INET, SOCK_STREAM)
		socket.connect((tgtHost, tgtPortS))
		socket.send('Hello')
		results = socket.recv(100)
		print('TCP Open: ' + str(tgtPortS) + '\n')
		print('Results: ' + str(results))
		exit(0)
	except:
		print('TCP Closed: ' + str(tgtPortS))

def portScan(tgtHost, tgtPort):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print('Cannot Resolve: Unknow Host: ' + tgtIP)
		return
	try: 
		tgtName = gethostbyaddr(tgtIP)
		print('Scan Results for: ' + tgtName[0])
	except:
		print('Scan Results for: ' + tgtIP)
	setdefaulttimeout(1)
	i = int(tgtPort)
	while i < 65535:
		print('Scanning Port: ' + tgtPort)
		connScan(tgtHost, int(i))
		i = i + 1

def main():
	parser=optparse.OptionParser('usage %prog –H '+'<target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type ='int', help='specify target port')
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPort = options.tgtPort
	if(tgtHost == None) | (tgtPort == None):
		print(parser.usage)
		exit(0)
	portScan(tgtHost, str(tgtPort))
if __name__ == '__main__':
	main()