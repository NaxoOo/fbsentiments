from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#import facebook
import urllib
from urllib.parse import urlparse
import subprocess
import warnings

import oauth2 as oauth


def connect(request):
	consumer_key = '279983135533947'
	consumer_secret = '9ff237e023f95b524274adef3af1ea21'

	redirect_uri = 'https://fbsentiments.azurewebsites.net/status/authorize'

	request_token_url = 'https://www.facebook.com/dialog/oauth?client_id=' + consumer_key
	+ '&redirect_uri=' + redirect_uri
	+ '&scope=user_posts'
	access_token_url = 'https://graph.facebook.com/v2.3/oauth/access_token?client_id=' + consumer_key
	+ '&redirect_uri=' + redirect_uri
	+ '&client_secret=' + consumer_secret
	+ '&code='#{code-parameter}
	#authorize_url = 'https://api.twitter.com/oauth/authorize'
	#Authorization URL: https://www.facebook.com/dialog/oauth (the scopes that can be specified with this URL, can be found here)

	consumer = oauth.Consumer(consumer_key, consumer_secret)
	client = oauth.Client(consumer)

	# Step 1: Get a request token. This is a temporary token that is used for 
	# having the user authorize an access token and to sign the request to obtain 
	# said access token.

	resp, content = client.request(request_token_url, "GET")
	#OJO: revisar error code (cuando sepa el formato)
	#https://developers.facebook.com/docs/graph-api/using-graph-api/#errors
	#if resp['status'] != '200':
	    #raise Exception("Invalid response %s." % resp['status'])

	request_token = dict(urlparse.parse_qsl(content))

	#print "Request Token:"
	#print "    - oauth_token        = %s" % request_token['oauth_token'] #Ver nombre en documentación de facebook.
	#print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
	#print 

	return HttpResponse("Hello, world. You're at the polls index.")
    #https://www.facebook.com/dialog/oauth?client_id=279983135533947&redirect_uri=https://fbsentiments.azurewebsites.net/status/authorize&scope=user_posts

def authorize(request):
	return HttpResponse("Holi, esto falta.")