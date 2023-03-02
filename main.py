from flask import Flask, render_template, request, redirect, url_for
import psycopg2


Lasertag = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect("postgres://ospqdsgchpdlxv:119a2e98fbf353a9cbc03a25dbe4ed8cc8ff4d22fbc377e200399084507f7506@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4hsfg0607dsnf", sslmode = 'require') 

    return conn

@Lasertag.route('/')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM player;')
    players = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('PlayerEntryScreen.html', player=players)

@Lasertag.route('/GamePlayScreen', methods=['GET','POST'])
def GamePlayScreen():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('GamePlayScreen.html')


if __name__ == '__main__':
    Lasertag.run()