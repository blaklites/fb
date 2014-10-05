Python SDK for the Facebook Graph API
=====================================

**fb** is a Python SDK for the Facebook Graph API. 
The SDK provides three methods for interacting largely with facebook; 

1. **publish(),**
2. **get_object()**, and 
3. **delete()**

In addtion to the three, there is one helper method to view the structure of
objects returned from facebook.



Installation
=============
::

    sudo pip install fb



**Usage**
=========

1. Publishing to Facebook
=========================

Using the publish() method, you can create(aka publish) objects like: status update, wall post, a like, events and albums, etc. However, currently *photo upload* is not supported.

The method returns the id of the object created.

Please refer to `https://developers.facebook.com/docs/graph-api/reference/v2.1/ <https://developers.facebook.com/docs/graph-api/reference/v2.1/>`_. All publishing categories can be used with this method except "photos".


Examples
---------

**Essential bit**

Go to `developers.facebook.com/tools/explorer <http://developers.facebook.com/tools/explorer>`_ to generate test token. Then create the authentication with the token.::

    import fb
    token = "Copy_Paste_the_token_that_Facebook_gave_you"
    facebook = fb.graph.api(token)


**Post on the current user's wall**::

    facebook.publish(cat = "feed", id = "me", message = "My facebook status")
     
**Like an object(wall post, photo and anything thats likable in facebook) with id=object_id**::

    facebook.publish(cat = "likes", id = object_id)

**Comment on an objects thats commentable**::

    facebook.publish(cat = "comments", id = object_id, message = "My comment")

**Create an album**::

    facebook.publish(cat = "albums", id = "me", name = "Album Name", message = "Album Details")

**Create an event**::

    facebook.publish(cat = "events", id = "me", name = "My Event", start_time = "2013-10-16-12:20", end_time = "2013-10-18-14:30" )


**An important note**

In addition to 'cat' (the category) and 'id', *publish()* takes any parameter thats valid for the publish category(cat).
Like "message" for wall post, "name" for albums, nothing for likes, etc. 

Please check Facebook documentation for full list of valid parameters for each kind of publishing. If you find that a parameter is raising error, it is maybe due to this SDK does not support the parameter yet, please report such cases to the author as an issue.


2. Fetch Objects from Facebook
===============================

Objects can be fetched in two ways using the get_object() method. Fetch "single" object with  it's given "fields"  passed in a list. Or, retrieve "multiple" objects passed with their "ids" in a list. The method returns the object as python dictionary containing related fields.


Examples
--------

**Retrieve given fields for a single object**::

    object = facebook.get_object(cat = "single", id = object_id, fields = ["name", "email" ] )
    
**Retrieve ALL fields for a single object**::

    object = facebook.get_object(cat="single", id = object_id, fields = [ ] )
    
**Retrieve multiple objects**::

    object = facebook.get_object(cat = "multiple", ids = ['zuck', 'me'] )


3. Delete Objects
==================

Deleting objects is simple. Use the delete() method and pass the id of the object to be deleted. Note that a "like" has no id in facebook, so in case of deleting a "LIKE", you have to pass the id of the object liked and the category of the delete which is "likes". 


Examples
--------

**Delete a status**::

    facebook.delete(id = status_id)
    

**Delete a comment**::

    facebook.delete(id = comment_id)
    

**Delete a "Like"**::

    facebook.delete(cat = "likes", id = object_id)


    
4. The Helper Methods
======================

As of version 0.4.0, there is one helper method, **show_fields()**. Using this method, it is possible to view the structure of the objects returned by Facebook. This will help further manipulate the fetched objects for individual needs.
 

Examples
--------

**Get "friends" and "education" of the current user**::

    friends_and_education = facebook.get_object(cat = 'single', id = 'me', fields = ['friends', 'education'])

**Display the Structure of the object returned from facebook graph**::

    facebook.show_fields(friends_and_education) 


The method will print the following:


    education(list)

    ........school

    .................id

    .................name

    ........type

    ........year

    ...............id

    ...............name

    friends

    ........paging

    ...............next

    ........data(list)

    ...............name

    ...............id

    id


All of the above are dictionary keys with sub-keys. Some of the keys are prefixed by "(list)" which means their values are saved inside a list and should be accessed through indexing. 

In line with the structure, printed by the  method, we can access various parts of the object fetched from facebook as shown below.


**"name" of schools attended**::

    friends_and_education['education'][0]['school']['name']
    friends_and_education['education'][1]['school']['name'] and so on........
    
**"type" of the nth school in the object**::

    friends_and_education['education'][n]['type']
    
**"name" of the nth friend in the object**::

    friends_and_education['friends']['data'][n]['name']
    
**"name" and "id" of all friends**::

    friends_and_education['friends']['data']

    
Note
-----

The idea behind introducing the show_fields() method is to help developers get a visual of the internal structure of objects retrieved from facebook graph so that they can write their own methods easily to further meet their needs.



Feature request & Report bugs
==============================

For any feature-request or to report a bug, please use Github's link's on the right-side of the page. Thank you.
PreferencesEnglish