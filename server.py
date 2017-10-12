from flask import Flask, render_template, request, redirect

from mysqlconnection import MySQLConnector

app = Flask(__name__)

db = MySQLConnector('friendsdb')

@app.route('/')
def index():
    friends = db.query_db('SELECT * FROM friends')
    return render_template('index.html', friends = friends)

@app.route('/friends/<friend_id>')
def friend(friend_id):
    friend = db.query_db('SELECT * FROM friends WHERE id = %s', (friend_id,))
    return render_template('index.html', friends = friend)

@app.route('/new')
def new():
    return render_template('create_user.html')

@app.route('/create', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name  = request.form['last_name']
    occupation = request.form['occupation']
    
    query = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())'
    data = (first_name, last_name, occupation)

    db.query_db(query, data)
    return redirect('/')

app.run(debug=True)
