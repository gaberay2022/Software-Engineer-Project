from flask import Flask, render_template, request, redirect, url_for
import psycopg2


Lasertag = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect("postgres://ospqdsgchpdlxv:119a2e98fbf353a9cbc03a25dbe4ed8cc8ff4d22fbc377e200399084507f7506@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4hsfg0607dsnf", sslmode = 'require') 

    return conn

@Lasertag.route('/')
def home():
    return render_template('PlayerEntryScreen.html')

@Lasertag.route('/GamePlayScreen', methods=['GET','POST'])
def GamePlayScreen():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT codename FROM player')
    result1 = cur.fetchall()
    players=[]
    for x in result1:
        players.append(x[0])
    cur.close()
    conn.close()
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('GamePlayScreen.html', player=players)

@Lasertag.route('/PlayerEntryScreen', methods=['GET','POST'])
def DBInsert():
    if request.method == 'POST':
        fn = request.form['player-1-fn']
        ln = request.form['player-1-ln']
        cn = request.form['player-1-cn']
        print(fn, ln, cn)
    if (not fn) or (not ln) or (not cn):
        return render_template("PlayerEntryScreen.html")
    else:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO player (first_name, last_name, codename) VALUES(%s,%s,%s)', (fn,ln,cn))
        cur.close()
        conn.commit()
        conn.close()
        return render_template("PlayerEntryScreen.html")

if __name__ == '__main__':
    Lasertag.run()