menu = """
Bienvenido al conversor de mondedas 💰
1. Pesos colombianos
2. Pesos argentinos
3. pesos mexicanos

Elije una opcíon
"""

opcion = int (input (menu))

if opcion == 1:
    pesos = input ("¿Cuántos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

elif opcion == 2:
    pesos = input ("¿Cuántos pesos argentino tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

elif opcion == 3:
    pesos = input ("¿Cuántos pesos Mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

else: 
    print ('Ingresa una opción correcta')