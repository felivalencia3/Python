import math
import sys
print("This is a two player game, the person who will set the word should take the computer and not show the other")

word = input("Enter the word  that you want your friend to answer\n")
if word:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
          "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
          "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
          "\n\n\n\n\n\n\n\n\n\n\n\nLet The game begin")
    spaces = len(word)
    char_list = list(word)
    dashes = ""
    guesses = 0
    length = float(spaces)
    for space in range(0,spaces):
        dashes += " _ "
    guesses = math.ceil((spaces)*2.5)
    guesses_str = str(guesses)
    print("The word you have to guess has the following letters => "+dashes+" "+"("+str(spaces)+")"+"\nAnd you have "+guesses_str +" tries to guess")

    while guesses > 0:
        full_guess = input("Enter your guess:\n")
        guess = full_guess[:1]
        if char_list.count(guess) >= 1:
            char_list.pop(char_list.index(guess))
            print("Correct! You have "+str(len(char_list))+" letters remaining")
        if len(char_list) == 0:
            print("Congratulations you completed the word")
            sys.exit()
        else:
            guesses =  guesses-1
            print("Guesses remaining: "+str(guesses-1))



else:
    print("Please enter a valid word")