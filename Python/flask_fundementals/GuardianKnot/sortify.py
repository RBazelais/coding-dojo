from flask import Flask, render_template, redirect, request, session
import mysqlconnector from MySQLConnector
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

DB = MySQLConnector(app, 'ilvernormy')

@app.route('/')
def landing():
    return render_template('index.html')


@app.route('/houses')
def houses():
    query_string = 'SELECT ilvernormy.students AS student FROM ilvernormy.houses.name'
    results = DB.query_db(query_string)
    return render_template('houses.html')

@app.route('/sortify', methods = ['POST'])
def sortify():
    name = request.form['name']
    house = random.randInt(1, 4)
    data = {
        'name': name,
        'house': house
    }
    session['data'] = data
    query_string = "INSERT INTO students (name, house_id) VALUES(:name, :house)"
    return redirect('/houses')

app.run(debug=True)