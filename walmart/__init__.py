import markdown
import os
import shelve

# Import the framework
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# Create an instance of Flask
app = Flask(__name__)

# Create the API
api = Api(app)

@app.route("/")
def index():

    # Open the index.md file
    with open(os.path.dirname(app.root_path) + '/index.md', 'r') as markdown_file:

        # Read the content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)


class healthz(Resource):
    def get(self):

        stream = os.popen('stat /proc/1 |grep Modify | cut -d. -f1|cut -d " " -f 2,3 ')
        output = stream.read()
        uptime_out = "up since " + output.strip() + " UTC"

        return {'status': 'OK', 'version': '0.0.1', 'uptime': uptime_out}, 200

api.add_resource(healthz, '/healthz')
