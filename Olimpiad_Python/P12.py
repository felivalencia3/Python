def sumarHoras(minuto1,hora1,minuto2,hora2):
    horas = hora1+hora2
    if horas > 12:
        horas -= 12
    minutos = min1+min2
    if minutos > 60:
        minutos -= 60
        horas += 1
    print("Hora:",horas)
    print("Minuto:",minutos)
    return(horas,minutos)

hora1 = int(input("Hora:\n\t"))
min1 = int(input("Minuto: \n\t"))
hora2 = int(input("\n\n\n\nHora:\n\t"))
min2 = int(input("Minuto:\n\t"))
sumarHoras(min1,hora1,min2,hora2)