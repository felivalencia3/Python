consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vocales = ['a', 'e', 'i', 'o', 'u']
def mandarAtras(palabra):
    palabra.append(palabra[0])
    palabra.pop(0)
    return palabra
def latinCerdo(palabra):
    palabra = list(palabra)
    primeraConsonante = True
    while(primeraConsonante):
        if palabra[0] in vocales:
            break
        elif palabra[0] in consonantes:
            palabra = mandarAtras(palabra)
    palabra.append("ay")
    return "".join(palabra)
print(latinCerdo(input("Palabra:\n")))