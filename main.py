from flask import Flask, render_template, request, jsonify, session
import psycopg2
from udp_socket import recieve
import subprocess
import os


Lasertag = Flask(__name__)

a = None

def get_db_connection():
    conn = psycopg2.connect("postgres://ospqdsgchpdlxv:119a2e98fbf353a9cbc03a25dbe4ed8cc8ff4d22fbc377e200399084507f7506@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4hsfg0607dsnf", sslmode = 'require') 

    return conn

@Lasertag.route('/')
def home():
    with open("files/redTeam.txt", "w") as f:
        f.write("")
    with open("files/greenTeam.txt", "w") as f:
        f.write("")
    return render_template('PlayerEntryScreen.html')

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
            pass
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('INSERT INTO player (first_name, last_name, codename) VALUES(%s,%s,%s)', (fn[i],ln[i],cn[i]))
            cur.close()
            conn.commit()
            conn.close()
    for i in range(len(fn)):
        fn.pop()
        ln.pop()
        cn.pop()
        return render_template("PlayerEntryScreen.html")


@Lasertag.route('/LobbyScreen', methods=['GET', 'POST'])
def LoadLobby():
    fn=[]
    ln=[]
    red='Red'
    green='Green'
    for i in range(1,7):
        if request.method == 'POST':
            fname = request.form[f'player-{i}-fn']
            lname = request.form[f'player-{i}-ln']
            Lkey = request.form['lobby-id']
            fn.append(fname)
            ln.append(lname)
    for i in range(len(fn)):
        if (not fn[i]) or (not ln[i]):
            pass;
        else:
            conn = get_db_connection()
            cur = conn.cursor()
            if (i<11):
                cur.execute('UPDATE player SET Lobby_Key=%s, Team=%s WHERE first_name=%s AND last_name=%s', (Lkey, red, fn[i],ln[i]))
            else:
                cur.execute('UPDATE player SET Lobby_Key=%s, Team=%s WHERE first_name=%s AND last_name=%s', (Lkey, green, fn[i],ln[i]))
    cn=[]
    for i in range(len(fn)):
        fn.pop()
        ln.pop()
        cur.execute('SELECT codename FROM player WHERE first_name=%s AND last_name=%s', (fn[i],ln[i]))
        row = cur.fetchone()
        if row:
            cn.append(row[0])
    conn.commit()
    conn.close()
    return render_template('LobbyScreen.html', codename=cn)

@Lasertag.route('/GamePlayScreen', methods=['GET','POST'])
def GamePlayScreen():
    if request.method == "POST":
        Lkey = request.form['lobby-id']
    red_team=[]
    green_team=[]
    players=[]
    
    conn = get_db_connection()
    cur = conn.cursor()
    if Lkey:
        cur.execute('SELECT codename, Team FROM player')
        for row in cur.fetchall():
            cn = row[0]
            team = row[1]

            if team == "Red":
                red_team.append(cn)
            else:
                green_team.append(cn)
    else:    
        cur.execute('SELECT codename FROM player')
        result1 = cur.fetchall()
        for x in result1:
            players.append(x[0])
        half_len = len(players)//2
        first_half = players[:half_len]
        second_half = players[half_len:]
    for i in range(len(first_half)):
        if(i == 0):
            if(red_team):
                with open("files/redTeam.txt", "w") as f:
                    f.write(red_team[i])
            else:
                with open("files/redTeam.txt", "w") as f:
                    f.write(first_half[i])
        else:
            if(red_team):
                with open("files/redTeam.txt", "a") as f:
                    f.write("," + red_team[i])
            else:
                with open("files/redTeam.txt", "a") as f:
                    f.write("," + first_half[i])

    for i in range (len(second_half)):
        if(i == 0):
            if(green_team):
                with open("files/greenTeam.txt", "w") as f:
                    f.write(green_team[i])
            else:
                with open("files/greenTeam.txt", "w") as f:
                    f.write(second_half[i])
        else:
            if(green_team):
                with open("files/greenTeam.txt", "a") as f:
                    f.write("," + green_team[i])
            else:
                with open("files/greenTeam.txt", "a") as f:
                    f.write("," + second_half[i])
    cur.close()
    conn.close()
    global a
    cmd_line = ['python', 'python_traffic_generator.py']
    a = subprocess.Popen(cmd_line, cwd=os.path.dirname(os.path.realpath(__file__)), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    return render_template('GamePlayScreen.html', fh=first_half, sh=second_half, red_team=red_team, green_team=green_team)

@Lasertag.route('/recieve_traffic')
def recieve_traffic():
    return recieve()

@Lasertag.route('/sendRedTeam', methods=['GET'])
def sendRedTeam():
    with Lasertag.open_resource('files/redTeam.txt') as f:
        red_team = f.read()
        return red_team
    
@Lasertag.route('/sendGreenTeam', methods=['GET'])
def sendGreenTeam():
    with Lasertag.open_resource('files/greenTeam.txt') as f:
        green_team = f.read()
        return green_team

if __name__ == '__main__':
    Lasertag.run()