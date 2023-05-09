
import pymysql

schema_name = "DevOps"

# Establishing a connection to DB

conn = pymysql.connect(host='localhost', user='root', passwd='', db=schema_name)
conn.autocommit(True)
cursor = conn.cursor()
print("Connecting to DB is successful")
