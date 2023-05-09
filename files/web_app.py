from flask import Flask, request
from files.db_connector import cursor
from files.db_connector import conn
from datetime import date

app = Flask(__name__)

# supported methods
@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def get_user_name(user_id):
    if request.method == 'GET':
        try:
            # Define the query with placeholders for the variables
            sql = "SELECT * FROM DevOps.users WHERE  user_id = %s"

            # Execute the query with the values
            cursor.execute(sql, user_id)

            # Fetch the result(s) of the query
            result = cursor.fetchall()

            user_name = result[0][1]
            cursor.close()
            conn.close()

            return "<H1 id='user'>" + user_name + "</H1>"
        except:
            return "<H1 id='user'>" + "no such user " + user_id + "</H1>"


# todo elif for put and delete

app.run(host='127.0.0.1', debug=True, port=5000)
