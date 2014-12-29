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


def create():
	"""
	create and return instance that connect to facebook graph
	"""
	return  httplib.HTTPSConnection('graph.facebook.com')

def send_request(req_cat, con, req_str, kwargs):
	"""
	Sends request to facebook graph
	Returns the facebook-json response converted to python object
	"""
        try:
                kwargs = parse.urlencode(kwargs)    #python3x
        except:
                kwargs = urllib.urlencode(kwargs)   #python2x
        
        """
        Wrapper to keep TCP connection ESTABLISHED. Rather the connection go to
        CLOSE_WAIT and raise errors CannotSendRequest or the server reply with
        empty and it raise BadStatusLine
        """        
        try:
            con.request(req_cat, req_str, kwargs)      #send request to facebook graph
        except httplib.CannotSendRequest:
            con = create()
            con.request(req_cat, req_str, kwargs)

        try:
            res = con.getresponse().read()		   #read response
        except (IOError, httplib.BadStatusLine):
            con = create()
            con.request(req_cat, req_str, kwargs) 
            res = con.getresponse().read()  

        t = type(res)
        if type(res) == t:
                res = bytes.decode(res)
        return json.loads(res)                     #convert the response to python object

