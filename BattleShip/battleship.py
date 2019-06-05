# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
from time import sleep
import sys

__author__ = "Felipe Valencia"
__copyright__ = "Copyright (C) 2019 Felipe Valencia"
__license__ = "GNU"
__version__ = "1.0"

numRow = 6  # type: int
numCol = 6
board1 = [[False for column1 in range(numCol)] for row1 in range(numRow)]
board2 = [[False for column2 in range(numCol)] for row2 in range(numRow)]
board1[0][0] = True
board2[0][1] = True
board2[0][0] = True

damage1 = 0  # type: int
damage2 = 0  # type: int
score1 = 0  # type: int
score2 = 0  # type: int
miss1 = 0  # type: int
miss2 = 0


def setResults(player, results):
    global score1
    global damage1
    global miss1
    global score2
    global damage2
    global miss2
    if player == player1:
        score1 += results["score"]
        damage2 += results["damage"]
        miss1 += results["miss"]
        return results["bar"]
    elif player == player2:
        score2 += results["score"]
        damage1 += results["damage"]
        miss2 += results["miss"]
        return results["bar"]


def setShip1(coord1, coord2):
    coord1 = int(coord1)
    coord2 = int(coord2)
    board1[coord1][coord2] = True


def setShip2(coord1, coord2):
    coord1 = int(coord1)
    coord2 = int(coord2)
    board2[coord1][coord2] = True


def attackShip(enemyboard, myplayer):
    damage = 0
    score = 0
    miss = 0
    print("{0} Enter coordinates for your attack:\n".format(myplayer))
    attackcoords = askForCoords()
    row = attackcoords["row"]
    col = attackcoords["col"]
    row = int(row)
    foo = True
    col = int(col)
    if not enemyboard[row][col]:
        print("\nMiss...\n")
        miss += 1
        foo = False
    if enemyboard[row][col]:
        print("\n\tHIT!\n")
        enemyboard[row][col] = False
        score += 1
        damage += 1
    package = {
        "damage": damage,
        "score": score,
        "miss": miss,
        "bar": foo
    }
    return package


def checkForShip(coord1, coord2, board):
    currentBoard = board1
    if board == 2:
        currentBoard = board2
    if currentBoard[coord1][coord2]:
        return True
    elif not currentBoard[coord1][coord2]:
        return False
    return


def askForCoords():
    row = input("\nEnter Row Number:\n")
    col = input("\nEnter Column Number\n")
    if int(row) >= 6 or int(col) >= 6 or int(row) < 0 or int(col) < 0 or (not row) or (not col):
        print("Sorry, you can only enter numbers up to 5 and positive numbers")
        coords = askForCoords()
        row = coords["row"]
        col = coords["col"]
    return {
        "row": row,
        "col": col
    }


def player2Start():
    print("\n\n\n\n\nHello, " + player2)
    print("Let's start setting up your board")
    print("First we will set up your 1 space spy-ship:\n")
    for i in range(1):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board2[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip2(row, column)
    print("Done.\n")
    print("\nNow for your 2 space ship")
    for k in range(2):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board2[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip2(row, column)
    print("\n\nNow your 3 space ship")
    for x in range(3):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board2[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip2(row, column)
    print("\n\n4 space ship:")
    for x in range(4):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board2[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip2(row, column)
    print("\n\nAnd last but not least, the 5 Space Ship")
    for x in range(5):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board2[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip2(row, column)
    print("\n\n\n\n\n\tDone!")


def player1Start():
    print("Let's start setting up your board")
    print("First we will set up your 1 space spy-ship:\n")
    for i in range(1):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board1[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip1(row, column)
    print("Done.\n")
    print("\nNow for your 2 space ship")
    for k in range(2):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board1[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip1(row, column)
    print("\n\nNow your 3 space ship")
    for x in range(3):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board1[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip1(row, column)
    print("\n\n4 space ship:")
    for x in range(4):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board1[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip1(row, column)
    print("\n\nAnd last but not least, the 5 Space Ship")
    for x in range(5):
        coords = askForCoords()
        row = coords["row"]
        column = coords["col"]
        introw = int(row)
        intcol = int(column)
        if board1[introw][intcol]:
            print("\tYou have already placed a ship here")
            newcoords = askForCoords()
            row = newcoords["row"]
            column = newcoords["col"]
        setShip1(row, column)
    print("\n\n\n\n\n\tDone!")


def getRemainingShips():
    remainingShip1 = 0
    remainingShip2 = 0
    for x in board1:
        remainingShip1 += x.count(True)
    for j in board2:
        remainingShip2 += j.count(True)
    return {
        "ship1": remainingShip1,
        "ship2": remainingShip2
    }


print("Welcome to Felipe's Battleship game!")
sleep(2)
print("Enter the players name below")
player1 = input("Player1's Name:\n")
player2 = input("\nPlayer2's Name:\n")
fakeTable = [['0,0', '0,2', '0,3', '0,4', '0,5', '0,6'],
             ['2,0', '2,2', '2,3', '2,4', '2,5', '2,6'],
             ['3,0', '3,2', '3,3', '3,4', '3,5', '3,6'],
             ['4,0', '4,2', '4,3', '4,4', '4,5', '4,6'],
             ['5,0', '5,2', '5,3', '5,4', '5,5', '5,6'],
             ['6,0', '6,2', '6,3', '6,4', '6,5', '6,6']]
for row in fakeTable:
    print(row)
print("What you see above is the way that your board will be spread out\n\n\tYou will have 5 ships:\n")
print("1 battleship, takes 5 spaces\n1 cruiser that takes up 4 spaces\n1 submarine that takes up 3 spaces")
print("1 destroyer that takes 2 spaces\n1 spy ship that takes up 1 space")
print("{0}, take the computer and don't show your opponent".format(player1))
sleep(4)
ready = input("Ready? [y/n]\n")
if ready == "yes" or ready == "y" or ready == "Y":
    player1Start()
    print("You have 4 seconds to pass the computer to {0} so that they can set up".format(player2))
    sleep(4)
    player2Start()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLets Start!")
    print("{0} will start, please give back the computer".format(player1))
    sleep(2)

    remainObj = getRemainingShips()
    remaining1 = remainObj["ship1"]
    remaining2 = remainObj["ship2"]
    while remaining1 > 0 or remaining2 > 0:
        results = attackShip(board2, player1)
        setResults(player1, results)
        remainObj = getRemainingShips()
        remaining1 = remainObj["ship1"]
        remaining2 = remainObj["ship2"]
        if remaining1 <= 0:
            print("\n\nPlayer 2 has Won!!")

            sys.exit(500)
        elif remaining2 <= 0:
            print("\n\nPlayer 1 has Won!!")

            sys.exit(500)
        # Player 2
        results = attackShip(board1, player2)
        setResults(player2, results)
        remainObj = getRemainingShips()
        remaining1 = remainObj["ship1"]
        remaining2 = remainObj["ship2"]
        if remaining1 <= 0:
            print("\n\nPlayer 2 has Won!!")

            sys.exit(500)
        elif remaining2 <= 0:
            print("\n\nPlayer 1 has Won!!")

            sys.exit(500)

elif ready == "no" or ready == "n":
    print("Ok then")

    sys.exit()

else:
    print("Ok then")

    sys.exit()
