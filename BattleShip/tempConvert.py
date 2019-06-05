# Celsius to Fahrenheit
def CtoF():
    celsius = float(input("Enter the Celsius Value:\t"))
    print("Fahrenheit: {0}".format(round((celsius * 1.8 + 32), 2)))


# Fahrenheit to Celsius
def FtoC():
    fahrenheit = float(input("Enter the Fahrenheit Value:\t"))
    print("Celsius: {0}".format(round(((fahrenheit - 32) / 1.8), 2)))


# Converting to Kelvin
def CtoK():
    celsius = float(input("Enter the Celsius Value:\t"))
    print("Kelvin: {0}".format(round((celsius + 273.15), 2)))


def FtoK():
    fahrenheit = float(input("Enter the Fahrenheit Value:\t"))
    print("Kelvin: {0}".format(round((((fahrenheit - 32) / 1.8) + 273), 2)))


print("Enter the number for the desired conversion:\n1: C to F\n2: F to C\n3: C to K\n4: F to K")
tempchoice = int(input("Enter:\t"))
if tempchoice == 1:
    CtoF()
elif tempchoice == 2:
    FtoC()
elif tempchoice == 3:
    CtoK
elif tempchoice == 4:
    FtoK()
