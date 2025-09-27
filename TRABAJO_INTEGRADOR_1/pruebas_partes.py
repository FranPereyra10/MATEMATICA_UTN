
# Solicitar al usuario un número entero
numero = int(input("Ingrese un numero:  "))

# Lista para almacenar los dígitos binarios invertidos
binario_invertido = []

# Si el número es negativo, calcular el complemento a dos
if numero < 0:
    numero = numero * -1  # Convertir el número a positivo
    
    # Convertir el número a binario (invertido)
    while (numero) > 0:
        digito = numero % 2  # Obtener el dígito binario
        binario_invertido.append(digito)  # Agregar el dígito a la lista
        numero = numero // 2  # Eliminar el último dígito
    
    # Invertir la lista para obtener el binario correcto
    binario = binario_invertido[::-1]
    
    # Rellenar con ceros a la izquierda para tener 8 bits
    while len(binario) < 8:
        binario.insert(0, 0)
    
    # Calcular el complemento a 1 (invertir los bits)
    for i in range(len(binario)):
        if binario[i] == 1:
            binario[i] = 0
        elif binario[i] == 0:
            binario[i] = 1
    
    # Vector para sumar 1 y obtener el complemento a 2
    complemento_a_2 = [0, 0, 0, 0, 0, 0, 0, 1]
    
    # Suma binaria para obtener el complemento a 2
    resultado = []
    carry = 0  # Variable para el acarreo
    for i in range(len(complemento_a_2) - 1, -1, -1):
        suma = binario[i] + complemento_a_2[i] + carry  # Sumar bit, complemento y acarreo
        bit = suma % 2  # Obtener el bit resultante
        carry = suma // 2  # Calcular el nuevo acarreo
        resultado.insert(0, bit)  # Insertar el bit al inicio de la lista
    if carry == 1:
        resultado.insert(0, 1)  # Si hay acarreo final, agregarlo
    resultado_final = ''.join(str(i) for i in resultado)  # Unir los bits en una cadena
    print("El resultado es:")
    print(resultado_final)

# Si el número es positivo, mostrar su binario directo
elif numero > 0:
    while (numero) > 0:
        digito = numero % 2  # Obtener el dígito binario
        binario_invertido.append(digito)  # Agregar el dígito a la lista
        numero = numero // 2  # Eliminar el último dígito
    
    binario = binario_invertido[::-1]  # Invertir la lista para obtener el binario correcto
    binario_final = ''.join(str(i) for i in binario)  # Unir los bits en una cadena
    print(f"El numero transformado a binario es: ")
    print(binario_final)