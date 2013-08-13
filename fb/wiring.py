try:
  import httplib
except:
        import http.client as httplib
try:
        from urllib import parse
except:
        import urllib
try:
	import simplejson as json
except:
	import json


#create and return instance that connect to facebook graph
def create():
	return  httplib.HTTPSConnection('graph.facebook.com')


#Sends request to facebook graph
#Returns the facebook-json response converted to python object
def send_request(req_cat, con, req_str, kwargs):
        try:
                kwargs= parse.urlencode(kwargs)    #python3x
        except:
                kwargs= urllib.urlencode(kwargs)   #python2x
        con.request(req_cat, req_str, kwargs)      #send request to facebook graph
        res=con.getresponse().read()		   #read response
        t=type(res)
        if type(res) == t:
                res=bytes.decode(res)
        return json.loads(res)                     #convert the response to python object
