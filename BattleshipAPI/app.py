from flask import Flask,request

numRow = 6
numCol = 6
app = Flask(__name__)
board1 = [[ False for column1 in range(numCol)]for row1 in range(numRow)]
board2 = [[ False for column2 in range(numCol)]for row2 in range(numRow)]


@app.route('/attack')
def attack():
    attacked_board = request.args.get("to")


@app.route("/setup")
def setup():
    board = request.args.get("board")


@app.route("/board1")
def board1():
    firstboard = tuple(board1)
    print(firstboard)
    return firstboard


@app.route("/board2")
def board2():
    secondboard= tuple(board1)
    print(secondboard)
    return secondboard

if __name__ == '__main__':
    app.run()
