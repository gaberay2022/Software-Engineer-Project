from flask import Flask, render_template

Lasertag = Flask(__name__)

@Lasertag.route('/')
def home():
    return render_template('PlayerEntryScreen.html')

if __name__ == '__main__':
    Lasertag.run()