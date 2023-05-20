from flask import Flask, request
from db_connector import get_request
import os
import signal

app = Flask(__name__)


# supported methods
@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user_name(user_id):
    if request.method == 'GET':
        try:
            user_name = get_request(user_id)
            return "<H1 id='user'>" + user_name + "</H1>"
        except:
            return "<H1 id='user'>" + "no such user " + user_id + "</H1>"


@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return 'Server stopped'
    except:
        return 'Server failed to stop'


# todo elif for put and delete

app.run(host='127.0.0.1', debug=True, port=5001)
