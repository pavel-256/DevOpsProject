import pymysql
from flask import request
from datetime import date

schema_name = "DevOps"
dataBase = 'Devops.users'
dbColumns = 'user_name,user_id,creation_date'
# local users storage
users = {}

# Establishing a connection to the database
# host.docker.internal - for kubernetes
conn = pymysql.connect(host='localhost', user='root', passwd='', db=schema_name)

conn.autocommit(True)


def get_request(user_id):
    # Define the query with placeholders for the variables

    sql = f"SELECT * FROM {dataBase} WHERE  user_id = %s"

    # Execute the query with the values
    cursor.execute(sql, user_id)

    # Fetch the result(s) of the query
    result = cursor.fetchall()
    return result


def post_request(user_id):
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
    return user_name


def delete_request(user_id):
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

    return user_name


def put_request(user_id):
    # getting the json data payload from request
    request_data = request.json

    # treating request_data as a dictionary to get a specific value from key
    user_name = request_data.get('user_name')
    users[user_id] = user_name

    # Define the query with placeholders for the variables
    sql = f"UPDATE {dataBase} SET user_name = {user_name} WHERE user_id  = {user_id}"

    # Execute the query
    cursor.execute(sql)
    return user_name


# Getting a cursor from the database
cursor = conn.cursor()
