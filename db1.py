from urllib import request

from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_HOST'] = "localhost"

@app.route('/fetchdata', methods=['GET', 'POST'])
def display():
    if request.method == 'POST':
        details = request.form
        cur = pymysql.Connection.cursor()
        state = details('State')
        stateAb= details('StateAb')
        cur.execute("SELECT Customer.cID,Customer.city,Customer.name,Customer.stateAb,Customer.street,Customer.zipcode from Customer inner join state where State.state = state or State.stateAb=stateAb ")
        result = cur.fetchall()
        print(result)
        pymysql.Connection.commit()
        cur.close()
        return render_template('query1.html', result=result)


@app.route('/insertdata', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        details = request.form
        cur = pymysql.connection.cursor()
        cur.execute("INSERT INTO state VALUES('Alaska','AA'))")
        pymysql.connection.commit()
        cur.close()





@app.route('/')
def root():
    return render_template('index.html')
