# Función básica para el cálculo de la reparación sistémica, de acuerdo a la Ley 26773.

def calcular():
    vmib = float(input("Ingresa tu salario base: "))
    porc_incapac = float(input("Ingresa el porcentaje de incapacidad: "))
    edad = int(input("Ingresa tu edad al momento del accidente o de la primera manifestación invalidante: "))
    resultado = 53 * vmib * (porc_incapac/100) * (65/edad)
    print(format(resultado, '.2f'))

calcular()