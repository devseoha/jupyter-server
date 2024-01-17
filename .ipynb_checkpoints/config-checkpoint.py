import psycopg2
import os

db_host = os.environ['SQL_HOST']
db_user = os.environ['SQL_USER']
db_password = os.environ['SQL_PASSWORD']
db_name = os.environ['DATABASE']

conn = psycopg2.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    dbname=db_name
)