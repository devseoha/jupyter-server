import pymysql
import os

db_host = os.environ['SQL_HOST']
db_user = os.environ['SQL_USER']
db_password = os.environ['SQL_PASSWORD']
database = os.environ['DATABASE']

conn = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=database
)

print(conn)
