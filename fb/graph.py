import wiring   #for http connection, requests and responds, similar stuffs
import request  #for creating request string

class api:
  token=None #facebook token
	con=None   #facebook connection
	
	#set token and HTTP connection
	def __init__(self, token):
		self.token=token
		self.con=wiring.create()


	#This method is used for creating objects in the facebook graph.
	#The first paramter is "cat", tje category of publish. In addition to "cat"
	#"id" must also be passed and is catched by "kwargs"
	def publish(self,  cat, **kwargs):
		res=request.publish_cat1("POST", self.con, self.token,  cat, kwargs)    
		return res
	
	#This method is used for retrieving objects from facebook. "cat", the category, must be
	#passed. When cat is "single", pass the "id "and desired "fields" of the single object. If the 
	#cat is "multiple", only pass the "ids" of the objects to be fetched.
	def get_object(self,  cat, **kwargs):
		if 'id' not in kwargs.keys():
			kwargs['id']=''
		res=request.get_object_cat1(self.con, self.token, cat,  kwargs)
		return res
	
	#Used for deleting objects from the facebook graph. Just pass the id of the object to be 
	#deleted. But in case of like, have to pass the cat ("likes") and object id as a like has no id
	#itself in the facebook graph
	def delete(self,  **kwargs):	
		if 'cat' not in kwargs.keys():
			kwargs['cat']=''
		cat=kwargs['cat']
		del kwargs['cat']
		res=request.publish_cat1("DELETE", self.con, self.token,  cat, kwargs)
		return res
