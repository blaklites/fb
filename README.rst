******************************************************************
*fb: Python Sdk for the Facebook Graph Api. (Supports python 2.X)*
******************************************************************

| **fb** is a python sdk for the Facebook Graph Api. The sdk provides two 
| methods for interacting largely with facebook. One for publishing to facebook, 
| publish(), and another for retrieving objects from facebook as python dictionary, 
|  get_object()
| 
| **sudo pip install fb**
|


*1. Publishing to Facebook*
===========================
| For publishing, use the publish() method. At `developers.facebook.com/docs/reference/api/publishing/ <http://developers.facebook.com/docs/reference/api/publishing/>`_
| under **'Other  Objects'**, see list of publish categories except "photos". Publishing includes 
| wrirting wall post, liking objects, creating events and albums, etc. Currently photo 
| upload is not supported

====================================
 *Example of publishing to facebook*
====================================
|    import fb    
|    # Go to `developers.facebook.com/tools/explorer <http://developers.facebook.com/tools/explorer>`_ to generate test token
|    token="*the facebook token you are going to use*"
|    facebook=fb.graph.api(token)
|    
|    *#Post on the current user's wall*
|    facebook.publish(cat="feed", id="me", message="My faecbook status")
|     
|    *#Like an object(wall post, photo and anything thats likable in facebook) with id=object_id*
|    facebook.publish(cat="likes", id=object_id)
|
|    *#Comment on an objects thats commentable*
|    facebook.publish(cat="comments", id=object_id, message="My comment")
|
|    *#Create an album*
|    facebook.publish(cat="albums", id="me", name="Album Name", message="Album Details")
|
|    *Create an event*
|    facebook.publish(cat="events", id="me", name="My Event", start_time="2013-10-16-12:20", end_time="2013-10-18-14:30" )

*Important*
-----------
|    In addition to 'cat' (the category)  and 'id', publish takes any parameter thats
|    valid for the publish category(cat). Like "message" for wall post, "name" for albums, 
|    nothing for likes, etc. Check facebook doc for full list of valid parameters 
|    for each kind of publishing. If you find that a parameter is raising error, 
|    it maybe because this sdk does not yet support the parameter,please report such cases 
|    to the author.

*2. Fetch Objects from Facebook*
================================

| Objects can be fetched in two ways using the get_object() method. 
| Fetch "single" object with  it's given "fields"  passed in a list.
| Or retrieve "multiple" objects passed with their "ids" in a list.

=============================================
*Example of retrieving objects from facebook*
=============================================
|    *#Retrieve given fields for a single object*
|    object=facebook.get_object(cat="single", id=object_id, fields=["name", "email" ] )
|
|    *#Retrieve ALL fields for a single object*
|    object=facebook.get_object(cat="single", id=object_id, fields=[ ] )
|
|    *#Rertieve multiple objects*
|    object=facebook.get_object(cat="multiple", ids=['zuck', 'me'] )
