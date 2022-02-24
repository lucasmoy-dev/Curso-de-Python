# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad

peso = int(input('Ingrese su peso en kg'))
alturaEnCM = int(input('Ingrese su altura en cm'))
alturaEnMetros = alturaEnCM / 100
imc = peso / (alturaEnMetros * alturaEnMetros)

print('Su IMC es de ' + str(imc))

if imc < 20:
    print('Estado de delgadez')
if imc >= 20 and imc < 26:
    print('Peso normal')
if imc >= 26 and imc < 30:
    print('Estado de sobrepeso')
if imc >= 30:
    print('Estado de obesidad')