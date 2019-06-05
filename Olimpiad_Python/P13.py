def cuantasVeces(palabra,letra):
    count = palabra.count(letra)
    return count
str = input("Palabra:\n\t")
char = input("Letra:\n\t")
print(cuantasVeces(str,char))
