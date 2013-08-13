import settings
import wiring 


#Constructs a "POST" URL. The function is used by the publish method 
#First category of  "POST" url construction. Caling it first category because for 
#publishing photos or more complex stuffs, newer fucntions may have to be added to deal with "POST". 
def publish_cat1(method, con, token, cat, kwargs):
        req_str="/"+str( kwargs['id'] )+"/"+cat+'?'   	        #/id/category?
        del kwargs['id']
 	kwargs['access_token']=token 				#add access token tokwwargs
        res=wiring.send_request(method, con, req_str, kwargs)    
	return res



#Constructs the "GET" and "DELETE" URL. The functions is used by both the get_object and delete method 
#First Category of "GET and "DELETE" URL construction. Again calling it first category because more
#complex functions  maybe added later. 
def get_object_cat1(con, token, cat, kwargs):
	req_str="/"+kwargs['id']+"?"               #/id?
	req_str+="access_token="+token             #/id?@acces_token=......
	del kwargs['id']
	
	key=settings.get_object_cat1_param[cat]    #get the param name for the category(fields, ids)
	req_str+="&"+key+"="                       #/id?@acces_token=......key=
	if key in kwargs.keys():
		length=len( kwargs[key] )
		for i in range(length):
			if i==0:
				req_str+=kwargs[key][i]
			else:
				req_str+=","+kwargs[key][i]	
	else:
		return "Parameter Error"
	
	res=wiring.send_request("GET", con, req_str, '')
	return res
