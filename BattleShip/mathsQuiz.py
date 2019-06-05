import random
score = 0

def askQuestion(num1, num2, operation):
    global score
    userAnswer = 0
    print("{0} {1} {2}".format(num1, operation, num2))
    if (operation == "+"):
        correctAnswer = num1 + num2
        userAnswer = int(input("Enter answer:\t\n"))
        if (userAnswer == correctAnswer):
            print("\nCorrect")
            score += 1
        else:
            print("\nIncorrect.")
    elif (operation == "-"):
        correctAnswer = num1 - num2
        userAnswer = int(input("Enter answer:\t\n"))
        if (userAnswer == correctAnswer):
            print("\nCorrect")
            score += 1
        else:
            print("Incorrect.")
    elif (operation == "*"):
        correctAnswer = num1 * num2
        userAnswer = int(input("Enter answer:\t\n"))
        if (userAnswer == correctAnswer):
            print("\nCorrect")
            score += 1
        else:
            print("\nIncorrect.")


def getNumbers():
    package = {
        "first": random.randint(0, 12),
        "second": random.randint(0, 12)
    }
    return package


def randomOperation():
    operations = ["+", "-", "*"]
    return random.choice(operations)


print("Welcome to my Maths Quiz\nYour questions will be Addition, Subtraction or Multiplication")
ready = input("Ready to Start? [Y/n]")
if (ready == "Y" or ready == "y" or ready == ""):
    for i in range(7):
        print("Question {0}".format(i))
        operation = randomOperation()
        twoNumbers = getNumbers()
        firstNum = twoNumbers["first"]
        secondNum = twoNumbers["second"]
        askQuestion(firstNum,secondNum,operation)
    print("Your Final Score was {0}".format(score))
else:
    import sys
    print("ok.")
    sys.exit(200)
