math = 15000
physics = 20000

def cuantoPagar(a,b,p,q):
    mathTotal = (a*math) * (1-(p/100))
    phyTotal = (b*physics) * (1-(q/100))
    print(mathTotal+phyTotal)
    return (mathTotal+phyTotal)

a = int(input("A:\n\t"))
b = int(input("B:\n\t"))
p = int(input("p:\n\t"))
q = int(input("q:\n\t"))
cuantoPagar(a,b,p,q)