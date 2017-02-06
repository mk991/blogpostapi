#!/usr/bin/python
from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_restful import reqparse
import datetime
 
#Create a engine for connecting to SQLite3.
db = create_engine('sqlite:///blog.db')

app = Flask(__name__)
api = Api(app)

class Posts(Resource):
    def get(self):
        #Connect to databse
        conn = db.connect()
        #Perform query and return JSON data
        query = conn.execute("select * from posts")
        result = []
        for row in query.cursor.fetchall():
        	result += [{'post_id': str(row[0]), 'title':str(row[1]), 'body': str(row[2])}]
        return result

class Post(Resource):
    def post(self):
        conn = db.connect()
        dt = datetime.datetime.now() #Create a datetime acces object for a unique post_id
        
        parser = reqparse.RequestParser() #parser for the arguments received from the /posts endpoint
        parser.add_argument('title', type=str, help='Title of the post')
        parser.add_argument('body', type=str, help='Body of the post')
        args = parser.parse_args()

        title = args['title']
        body = args['body']
        date_time = int(dt.day)+int(dt.month)+int(dt.year)+int(dt.hour)+int(dt.minute)+int(dt.second) #sum of the date and time fields for unique post_id
        message = 'Empty fields : '
        if title == '':
            message += 'Title\n'
        if body == '':
            message += 'Body'

        if message != 'Empty fields : ':
            return message+'\n Can\'t submit.'

            
        query = conn.execute("insert into posts(post_id,title,body) values(?,?,?)", (str(date_time),title,body))
        return 'Post submitted successfully'
 
api.add_resource(Post, '/post')
api.add_resource(Posts, '/posts')

if __name__ == '__main__':
     app.run(host="127.0.0.1",debug=True, port=int('8080'))