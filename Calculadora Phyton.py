def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Función principal
def calculadora():
    print("Calculadora Simple")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Selecciona una operación (1/2/3/4): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print(num1, "+", num2, "=", sumar(num1, num2))
    elif opcion == '2':
        print(num1, "-", num2, "=", restar(num1, num2))
    elif opcion == '3':
        print(num1, "*", num2, "=", multiplicar(num1, num2))
    elif opcion == '4':
        print(num1, "/", num2, "=", dividir(num1, num2))
    else:
        print("Opción no válida. Por favor, selecciona una operación válida.")

# Llamada a la función principal
calculadora()
