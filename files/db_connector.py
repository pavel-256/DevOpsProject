import pymysql

schema_name = "DevOps"

# Establishing a connection to the database
conn = pymysql.connect(host='localhost', user='root', passwd='', db=schema_name)
conn.autocommit(True)

# Getting a cursor from the database
cursor = conn.cursor()



