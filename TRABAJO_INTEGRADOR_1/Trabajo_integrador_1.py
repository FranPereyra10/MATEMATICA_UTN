#Conversión de Números:
#Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
#Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.

#Comenzamos mostrando un msj de bienvenida:

print("Bienvenido al programa de conversion de numeros decimales a Binarios y de Binarios a Decimales.")

#solicitamos al usuario que elija que tipo de conversion desea realizar

opcion = int(input("Ingrese 1 para convertir un numero decimal a binario. \nIngrese 2 para convertir un numero binario a decimal. "))

if opcion == 1:
    numero_decimal = int(input("Ingrese el numero decimal que desea convertir: "))
    while int(numero_decimal/2) > 2:
        