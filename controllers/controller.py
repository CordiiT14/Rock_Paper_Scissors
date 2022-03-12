from flask import redirect, render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game

@app.route('/play')
def index():
    return render_template('index.html', title="Play!")

@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/play', methods=['GET','POST'])
def play():
        player_1_name = request.form['player1_name']
        player_1_choice = request.form['p1_choice']
        player_2_name = request.form['player2_name']
        player_2_choice = request.form['p2_choice']
        player1 = Player(player_1_name, player_1_choice)
        player2 = Player(player_2_name, player_2_choice)
        game = Game()
        game.add_players(player1)
        game.add_players(player2)
        winner= game.return_winner(game)
        winning_player = game.display_winner(player1, winner)
        return render_template('results.html', title='The Winner is..', winning_player=winning_player , winner=winner, player1=player1, player2=player2)


# Routes below used initially

# @app.route('/rock/scissors', )
# def rock_win():

#     return render_template('rock.html', title="Rock Wins")


# @app.route('/scissors/paper')
# def scissors_win():
#     return render_template('scissors.html', title='Scissors Wins' )


# @app.route('/paper/rock')
# def paper_win():
#     return render_template('paper.html', title='Paper Wins', )