from flask import Flask, render_template, request,redirect

from mysqlconnection import MySQLConnector

app= Flask(__name__)

mysql=MySQLConnector(app,"email_val")

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)

    return render_template('index.html',users=users)

@app.route('/register', methods=["POST"])
def register():
    query= "INSERT INTO users (email, created_at, updated_at) VALUES (:emailname, NOW(), NOW() )"
    data={
        'emailname': request.form['email']
    }
    mysql.query_db(query,data)
    return redirect('/')



app.run(debug=True)
