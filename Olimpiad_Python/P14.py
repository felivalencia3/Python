import math
def distanciaRectangulo(p1,p2):
    return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))


x_esquina = int(input("X:\n"))
y_esquina = int(input("Y:\n"))
x_punto = int(input("X:\n"))
y_punto = int(input("Y:\n"))
print(distanciaRectangulo((x_esquina,y_esquina),(x_punto,y_punto)))