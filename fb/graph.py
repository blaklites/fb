import wiring   #for http connection, requests and responds, similar stuffs
import request  #for creating request string

class api:
  token=None #facebook token
	con=None   #facebook connection
	
	#set token and connection
	def __init__(self, token):
		self.token=token
		self.con=wiring.create()

	def publish(self,  cat, **kwargs):
		res=request.publish_cat1("POST", self.con, self.token,  cat, kwargs)    
		return res
	
	def get_object(self,  cat, **kwargs):
		if 'id' not in kwargs.keys():
			kwargs['id']=''
		res=request.get_object_cat1(self.con, self.token, cat,  kwargs)
		return res
	
	def delete(self,  **kwargs):	
		if 'cat' not in kwargs.keys():
			kwargs['cat']=''
		cat=kwargs['cat']
		del kwargs['cat']
		res=request.publish_cat1("DELETE", self.con, self.token,  cat, kwargs)
		return res
