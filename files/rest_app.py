from flask import Flask, request
from files.db_connector import cursor
from files.db_connector import conn
from datetime import date

app = Flask(__name__)

# local users storage
users = {}

# table in db
dataBase = 'Devops.users'
dbColumns = 'user_name,user_id,creation_date'


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':

        try:
            # Define the query with placeholders for the variables
            sql = f"SELECT * FROM {dataBase} WHERE  user_id = %s"

            # Execute the query with the values
            cursor.execute(sql, user_id)

            # Fetch the result(s) of the query
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return {'user id': user_id, 'user name': result[0][1], 'status': 'ok'}, 200
        except:
            return {'reason': 'no such id', 'status': 'error'}, 400

    elif request.method == 'POST':

        # getting the json data payload from request
        request_data = request.json

        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        users[user_id] = user_name

        # Define the query with placeholders for the variables
        sql = f"INSERT INTO {dataBase}  ({dbColumns}) VALUES(%s,%s,%s)"

        # Execute the query with the values
        values = (user_name, user_id, date.today())

        # Execute the query with the values
        cursor.execute(sql, values)

        # Close the connection and cursor
        cursor.close()
        conn.close()
        return {'user id': user_id, 'user_added': user_name, 'status': 'ok'}, 200  # status code

    elif request.method == 'DELETE':

        try:
            # getting the json data payload from request
            request_data = request.json

            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            users[user_id] = user_name

            # Define the query with placeholders for the variables
            sql = f"DELETE FROM {dataBase} WHERE user_id = %s;"

            # Execute the query with the values
            values = (user_id,)

            # Execute the query with the values
            cursor.execute(sql, values)

            # Close the connection and cursor
            cursor.close()
            conn.close()
            return {'user id': user_id, 'user_deleted': user_name, 'status': 'ok'}, 200  # status code

        except:
            return {'status': "error", 'reason': 'no such id'}, 500  # status code

    elif request.method == 'PUT':

        try:
            # getting the json data payload from request
            request_data = request.json

            # treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            users[user_id] = user_name

            # Define the query with placeholders for the variables
            sql = f"UPDATE {dataBase} SET user_name = {user_name} WHERE user_id  = {user_id}"

            # Execute the query
            cursor.execute(sql)

            # Close the connection and cursor
            cursor.close()
            conn.close()
            return {'user_updated': user_name, 'status': 'ok'}, 200  # status code

        except:
            return {'status': "error", 'reason': 'no such user id'}, 500  # status code


# todo elif for put and delete

app.run(host='127.0.0.1', debug=True, port=5000)
