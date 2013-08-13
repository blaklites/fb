try:
  import httplib
except:
	import http.client as httplib
import urllib
try:
	import simplejson as json
except:
	import json


#create and return instance that connect to facebook graph
def create():
	return  httplib.HTTPSConnection('graph.facebook.com')


#Sendrequest to facebook graph
#Return the facebook-json response converted to python object
def send_request(req_cat, con, req_str, kwargs):
	kwargs= urllib.urlencode(kwargs)           #keep the url consistent spaces and any special characters
	con.request(req_cat, req_str, kwargs)      #send request to facebook graph
	res=con.getresponse().read()		   #read response
	return json.loads(res)                     #convert the response to python object
	
