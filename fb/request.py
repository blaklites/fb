from . import settings
from . import wiring 


#Constructs a "POST" and "DELETE" URL. The function is used by the publish and delete method
#First category of  "POST" and "DELETE" url construction. Caling it first category because for 
#publishing photos or more complex stuffs, newer fucntions might be added to deal with "POST". 
def publish_cat1(method, con, token, cat, kwargs):
        req_str="/"+str( kwargs['id'] )+"/"+cat+'?'                #/id/category?
        del kwargs['id']
        kwargs['access_token']=token                               #add access token to kwwargs
        res=wiring.send_request(method, con, req_str, kwargs)    
        return res



#Constructs the "GET" URL. The functions is used by the get_object method
#First Category of "GET" URL construction. Again calling it first category because more
#complex functions  maybe added later. 
def get_object_cat1(con, token, cat, kwargs):
        req_str="/"+kwargs['id']+"?"               #/id?
        req_str+="access_token="+token             #/id?@acces_token=......
        del kwargs['id']
        
        key=settings.get_object_cat1_param[cat]    #get the param name for the category(single, multiple)
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
