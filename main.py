from flask import Flask, render_template, request, redirect, url_for
import psycopg2

i=1;
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
    fn=[]
    ln=[]
    cn=[]
    for i in range(1,7):
        if request.method == 'POST':
            fname = request.form[f'player-{i}-fn']
            lname = request.form[f'player-{i}-ln']
            cname = request.form[f'player-{i}-cn']
            fn.append(fname)
            ln.append(lname)
            cn.append(cname)
    for i in range(len(fn)):
        if (not fn[i]) or (not ln[i]) or (not cn[i]):
            pass;
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO player (first_name, last_name, codename) VALUES(%s,%s,%s)', (fn[i],ln[i],cn[i]))
            cur.close()
            conn.commit()
            conn.close()
    for i in range(len(fn)):
        fn.pop
        ln.pop
        cn.pop
        return render_template("PlayerEntryScreen.html")

if __name__ == '__main__':
    Lasertag.run()