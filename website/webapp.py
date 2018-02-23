import mysql.connector
from flask import Flask
from flask import render_template
from flask import request
from flask import g


app = Flask(__name__)
app.debug = True

cnx = mysql.connector.connect(user='root', password='***', database='***', host='localhost')
cursor = cnx.cursor()


@app.route("/")
def show():

    cursor.close()
    cnx.close()


if __name__ == "__main__":
    app.run()
