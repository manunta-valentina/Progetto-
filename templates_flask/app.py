from flask import render_template
from flask import Flask

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "Netflix_Originals"
)

mycursor = mydb.cursor()

app = Flask(__name__)


@app.route('/')
def unitList():
    mycursor.execute("SELECT * FROM Netflix_Unit")
    myresult = mycursor.fetchall()
    return render_template('Netflix_Unit.html', units=myresult)


@app.route('/details/<id>')
def movieDetail(id):
    mycursor.execute("SELECT * FROM Netflix_Unit where ID = '{}'".format(id))
    myresult = mycursor.fetchall()
    return render_template('Netflix_Details.html', details=myresult)

