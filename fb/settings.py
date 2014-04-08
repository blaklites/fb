"""
The dictionary in this file is just for paramter validity checking.
It is used by the get_object_cat1 function in the request.py file
to ensure that the paramters passed for each category in the get_object  
method is valid. The file is actualy intented for customization of the sdk
through a single settings file. Keep eye on future versions 
"""

get_object_cat1_param={"single":"fields", "multiple":"ids" } 


#Note. Similar dictionaries can be made in order to keep
#paramter check for the publish and delete method. 
