
import sys
from two1.wallet import Wallet
from two1.bitrequests import BitRequests

#set up the wallet for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

#server url
server_addr = 'http://[::1]:5000'


def end_point():
#response from the server in the form of text
	response = requests.get(server_addr.format(text))

#prints the response
	print(response.text)

if __name__ == '__main__'
	end_point(sys.argv[1])


