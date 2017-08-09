
from flask import Flask, request
from uber_rides.session import Session

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app,wallet)

#create a session
session = Session(server_token='token obtained from uber')

#create a client
client = UberRidesClient(session)



@app.route('/')
@payment.required(2000)


def uber_rides():
#get the available product within a loaction
	products = client.get_products(longitude, latitude)

#get the estimate of the product to our destination
	estimate =  client.estimate_ride(product_id=' ', start_latitude= , start_longitude= , start_place_id='None', end_latitude=, end_longitude='', end_place_id='None', seat_count=None)

#request the ride
	request = client.request_ride(product_id='', start_latitude= , start_longitude= , start_place_id= , start_address=None, start_nickname=none, end_latitude= , end_longitude=None, end_place_id=None, end_address=None, end_nickname=None, seat_count=None, fare_id=None, surge_confirmation_id=None, payment_method_id='')

	#return product, estimate, request

if __name__ == '__main__':
	app.run(host='::')
	
