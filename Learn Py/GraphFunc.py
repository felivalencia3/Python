from math import sqrt
def graphFunc(x):
    return 4/sqrt(x)


for x in range(1,18):
    print(x , "--->\t" , graphFunc(x))
