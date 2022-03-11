from flask import render_template, request
from app import app
from models.player import Player
from models.game import Game

@app.route('/play')
def index():
    return render_template('index.html', title="Play!")

@app.route('/rock/scissors')
def rock_win():
    return render_template('rock.html', title="Rock Wins")

@app.route('/scissors/paper')
def scissors_win():
    return render_template('scissors.html', title='Scissors Wins', )

@app.route('/paper/rock')
def paper_win():
    return render_template('paper.html', title='Paper Wins', )

