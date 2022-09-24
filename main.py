from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console


first = Game('Tetris', 'Puzzle', 'Atari')
second = Game('God of War', 'War', 'PS2')
third = Game('Mortal Kombat', 'Fight', 'PS2')
games = [first, second, third]


@app.route('/')
def index():
    return render_template('list.html', titulo='Game List', games=games)


@app.route('/newgame')
def form():
    return render_template('insert.html', titulo='New Game')


@app.route('/new', methods=['POST', ])
def new():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']
    new_game = Game(name, category, console)
    games.append(new_game)

    return redirect('/')


app.run(host='0.0.0.0', port=8080, debug=True)
