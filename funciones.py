def conversor(tipo_pesos, valor_dolar):
    pesos = input ("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """
Bienvenido al conversor de mondedas 💰
1. Pesos colombianos
2. Pesos argentinos
3. pesos mexicanos

Elije una opcíon
"""

opcion = int (input (menu))

if opcion == 1:
    conversor("colombianos", 3875)

elif opcion == 2:
    conversor("Argentinos", 65)

elif opcion == 3:
    conversor("Mexicanos", 24)

else: 
    print ('Ingresa una opción correcta')