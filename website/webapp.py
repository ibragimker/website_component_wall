import mysql.connector
from flask import Flask
from flask import render_template
from flask import request
from flask import g


app = Flask(__name__)
app.debug = True

cnx = mysql.connector.connect(user='root', password='Tn171129', database='hamidtoufik_databank', host='localhost')
cursor = cnx.cursor()






@app.route('/')
def searchbar():
    return render_template('searchbar.html')

    cursor.close()
    cnx.close()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)