import matplotlib.pyplot as plt
import sys


def plotPoints(m,b,indice):
    coords = []
    for x in range(-50,60):
        bar = m*((x/10)**indice)+b
        coords.append(bar)
    return coords
def printPoints(m,b,indice):
    coordinates = []
    for t in range(-5,6):
        qux = m*(t**indice)+b
        coordinates.append(qux)
    return coordinates
def graphIt(x,y):
    plt.plot(x,y)
    plt.show()
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print("\n")
print( color.UNDERLINE+"Hint: For a better experience, run this in terminal with the python command"+color.END)
print( color.RED + "Welcome to Felipe's Graph Program!\n" + color.END)
print("To start you need an equation like this: \t "+color.PURPLE+"y=mx+c"+color.END)

print("Where m is the gradient and c is the addition or subtraction\n\nTake for example this equation:\t"+color.YELLOW+"y=2x+3"+color.END)
foo = input("\n\n\tReady? [Y/N]")
if foo == "Y" or foo=="y":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Let's Start:")
    gradient = float(input("\nEnter the Gradient of your equation (m)\n\t"))
    increment = float(input("\nNow enter the addition or subtraction of your equation (c)\n\t"))
    print("\n\nNow on to exponents:")
    print("Is your equation linear (x) ,quadratic (x^2) or cubic (x^3)?\n")
    exponent = int(input("\nEnter 1 for linear, 2 for quadratic and 3 for cubic\n\t"))
    xCoords = []
    for j in range(-50,60):
        xCoords.append(j/10)

    printX = []
    for rawr in range(-5,6):
        printX.append(rawr)
    print("x points:",printX)
    yCoords = plotPoints(gradient,increment,exponent)
    printY = printPoints(gradient,increment,exponent)
    print("y points:",printY)
    graphIt(xCoords,yCoords)
elif foo == "N" or foo=="n":
    print("Ok then. Bye")
    sys.exit()
else:
    print("Enter a valid command: yes or no")