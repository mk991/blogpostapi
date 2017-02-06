# blogpostapi
Blogpost api to write single post to the database and to reterive a list of all posts from the database in Python and data exchange in JSON
Prerequisites:
Install Python 2 >=2.7.9 
Install flask microweb framework 
Install flask-restful 

For testing purpose use an extension such as "Postman" - available in chrome.

http://127.0.0.1:8080/post - [POST Method] - The form-data contains keys - title, body and values can be any string. http://127.0.0.1:8080/posts - [GET Method] - The data will be received in JSON. Contains all the post_id, title and body values in the sqlite database.

Make sure you run the blogpost.py first on your IDE or command-line and then access the URL.

Check the comments in the blogPostApi.py for more details on how the code works.
