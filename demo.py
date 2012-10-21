from oauth_twitter import TwitterRequest, TwitterConsumer
import json

try:
	from config import CONSUMER_KEY, CONSUMER_SECRET, CALLBACK_URL
	from config import ACCESS_TOKEN, ACCESS_SECRET
except:
	# required
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''

	# required if you want the demo of access_token obtaining
	CALLBACK_URL = ''

	# required if you want the demo of accessing user data only
	ACCESS_TOKEN = ''
	ACCESS_SECRET = ''

def obtain_token(tc):
	print "Step #1: request_token"
	tc.request_token()

	print "Step #2: authenticate"
	tc.authenticate()
	
	print "Step #3: access_token"
	tc.access_token()

def access_userdata(tc):
	print "Acquiring @twitter's profile..."	
	tr = TwitterRequest("GET", "https://api.twitter.com/1.1/users/show.json?screen_name=twitter" )
	response = tc.get_response( tr )
	data = response.read()
	jdata = json.loads( data )
	print json.dumps( jdata, sort_keys = True, indent=4 )

if __name__ == '__main__':
	tc = TwitterConsumer(
		CONSUMER_KEY, 
		CONSUMER_SECRET, 
		CALLBACK_URL)

	answer = raw_input( "Run access_token obtaining demo?(Y/n)" )
	if answer != 'n':
		obtain_token( tc )

	tc.a_token = ACCESS_TOKEN
	tc.a_secret = ACCESS_SECRET
	answer = raw_input( "Run user data accessing demo?(Y/n)" )
	if answer != 'n':
		access_userdata( tc )