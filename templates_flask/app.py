from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/')
def unitList():
    mycursor.execeute ("SELECT * FROM Netflix_Unit")
    myresul = mycursor.fetchall()
    return render_template('Netflix_Units.html', units=myresult)

