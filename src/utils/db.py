import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

def connect_db():
    return pymysql.connect(
        host='mysql',
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', ''),
        database=os.getenv('MYSQL_DATABASE', 'youfoodie')
    )

conn = connect_db()