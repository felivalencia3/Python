def triangulo(altura,letra):
    for i in range(altura):
        print(i*letra)
altura = int(input("Altura:\n"))
letra = input("Letra:\n")
triangulo(altura,letra)