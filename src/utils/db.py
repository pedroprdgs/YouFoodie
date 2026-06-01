import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db():
    return pymysql.connect(
        host=os.getenv('MYSQL_HOST', 'localhost'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DATABASE', 'youfoodie'),
        cursorclass=pymysql.cursors.DictCursor
    )

def fetch_data(query, params=None):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    finally:
        conn.close()

def execute_query(query, params=None, return_lastrowid=False):
    conn = connect_db()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            conn.commit()
            if return_lastrowid:
                return cursor.lastrowid
    finally:
        conn.close()
