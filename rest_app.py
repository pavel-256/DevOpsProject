import signal
from flask import Flask, request

from db_connector import get_request, post_request, delete_request, put_request
import os
from datetime import date

# local users storage
users = {}

app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            # Get username from request
            result = get_request(user_id)
            return {'user id': user_id, 'user name': result[0][1], 'status': 'ok'}, 200

        except:
            return {'reason': 'no such id', 'status': 'error'}, 400

    elif request.method == 'POST':

        try:
            # Get username from request
            user_name = post_request(user_id)
            return {'user id': user_id, 'user_added': user_name, 'status': 'ok'}, 200  # status code

        except:
            return {'status': "error", 'reason': 'id already exist'}, 500  # status code

    elif request.method == 'DELETE':

        try:
            # Get username form request
            user_name = delete_request(user_id)
            return {'user id': user_id, 'user_deleted': user_name, 'status': 'ok'}, 200  # status code

        except:
            return {'status': "error", 'reason': 'no such id'}, 500  # status code

    elif request.method == 'PUT':

        try:
            user_name = put_request(user_id)
            return {'user_updated': user_name, 'status': 'ok'}, 200  # status code

        except:
            return {'status': "error", 'reason': 'no such user id'}, 500  # status code


@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return 'Server stopped'
    except:
        return 'Server failed to stop'


app.run(host='127.0.0.1', debug=True, port=5000)
