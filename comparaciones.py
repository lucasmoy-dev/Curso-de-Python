nombre = input('¿Cómo te llamas?')
print('Hola ' + nombre)

edad = int(input('¿Cuántos años tienes?'))
masDe12 = edad >= 12
respuestaHijoDelDueño = input('¿Eres hijo del dueño?')
esHijoDelDueño = respuestaHijoDelDueño == 'si'
puedePasar = masDe12 or esHijoDelDueño

if puedePasar:
    print('Usted puede pasar a la montaña rusa')
else:
    print('No puede pasar')


def mostrarPrecioFinal(producto, precio, descuento):
    precioFinal = precio - descuento * precio / 100
    print("El precio del " + producto + " es: $" + str(precioFinal))

mostrarPrecioFinal("Pantalón", 40, 20)
mostrarPrecioFinal("Pantalón", 30, 15)