from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import psycopg2
import threading
from python_traffic_generator import generate_traffic

i=1
Lasertag = Flask(__name__)
Lasertag.config['SECRET_KEY'] = 'secret!'
socketio=SocketIO(Lasertag)

def get_db_connection():
    conn = psycopg2.connect("postgres://ospqdsgchpdlxv:119a2e98fbf353a9cbc03a25dbe4ed8cc8ff4d22fbc377e200399084507f7506@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4hsfg0607dsnf", sslmode = 'require') 

    return conn

@Lasertag.route('/')
def home():
    return render_template('PlayerEntryScreen.html')

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

#working on setting up sockets
# @socketio.on('generate_traffic')
# def traffic_generator(data):
#         red_team1 = data['red_team1']
#         red_team2 = data['red_team2']
#         green_team1 = data['green_team1']
#         green_team2 = data['green_team2']
#         count = data['count']
#         generate_traffic(udp, red_team1, red_team2, green_team1, green_team2, count)
#         return jsonify({'success': True})

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
        #generate_traffic(udp, red_team[0], red_team[1], green_team[0], green_team[1], 20)
    else:    
        cur.execute('SELECT codename FROM player')
        result1 = cur.fetchall()
        for x in result1:
            players.append(x[0])
        half_len = len(players)//2
        first_half = players[:half_len]
        second_half = players[half_len:]
        #generate_traffic(udp, first_half[0], first_half[1], second_half[0], second_half[1], 20)
    cur.close()
    conn.close()
    #traffic generator code here
    #message = udp.receive_message
    return render_template('GamePlayScreen.html', fh=first_half, sh=second_half, red_team=red_team, green_team=green_team)#, message=message)

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

if __name__ == '__main__':
    socketio.run(Lasertag)