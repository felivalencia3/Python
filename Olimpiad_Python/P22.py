names = []
def nombreRepetido():
    for name in names:
        if names.count(name) > 1:
            tocayo = names[names.index(name)]
            return tocayo
    return

n = int(input("n:\n"))
for i in range(n):
    names.append(input("\nNombre:\n"))
tocayo = nombreRepetido()
if tocayo:
    print("SI {}".format(tocayo))
else:
    print("NO")