from flask import Flask
import mysql.connector

app = Flask(__name__)

from views import *
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="suzuki",
        database="gamerate"
    )


if __name__ == "__main__":
    app.run()