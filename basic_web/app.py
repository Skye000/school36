from flask import Flask, render_template
from db import DB_maneger

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')
@app.route("/allinfo")
def allinfo():
    return render_template('allinfo.html')

@app.route("/show")
def show():

    try:
        users = DB_maneger('users.db')
        listuser=users.fetchall('''SELECT * FROM Users''')

    except:
        listuser=[('База', 'без','данных')]

    print(listuser)
    users.create_tables()

    # vl=('Vasya', 'Ivanov', 'vasya.iv@gmail.com')
    #
    # users.qery('''INSERT INTO Users VALUES(?, ?, ?)''', vl)
    # users.qery('''DELETE FROM Users VAlUES(?, ?, ?)''')
    return render_template('show.html', listuser=listuser)

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/read_form', methods=['POST'])
def read_form():
    users=DB_maneger('users.db')
    users.create_tables()
    data=request.form
    userEmail=data['userEmail']
    userName=data['name']
    userLastName = data['lastname']
    dictsend=(userEmail,userName,userLastName)
    print(*dictsend)

    users.qery('INSERT INTO Users VALUES (?,?,?)', dictsend)

    return render_template('read_form.html')



if __name__=="__main__":
    app.run(debug=True)



