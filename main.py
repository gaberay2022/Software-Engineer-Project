from flask import Flask, render_template
import os
import psycopg2

conn = psycopg2.connect('postgres://ospqdsgchpdlxv:119a2e98fbf353a9cbc03a25dbe4ed8cc8ff4d22fbc377e200399084507f7506@ec2-3-217-251-77.compute-1.amazonaws.com:5432/d4hsfg0607dsnf', sslmode = 'require') 

Lasertag = Flask(__name__)

@Lasertag.route('/')
def home():
    return render_template('PlayerEntryScreen.html')

if __name__ == '__main__':
    Lasertag.run()