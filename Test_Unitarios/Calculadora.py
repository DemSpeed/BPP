''' Calculadora Con Funciones en Python
    Autor: Javier Villa Sarmentero '''

# Función para sumar
def Sumar(x, y):
    return x + y

# Función para restar
def Restar(x, y):
    return x - y

# Función para multiplicar
def Multiplicar(x, y):
    return x * y

# Función para dividir
def Dividir(x, y):
    return x / y

# Menú selección
print("Bienvenido")
print("1.Suma")
print("2.Resta")
print("3.Multiplicar")
print("4.Dividdir")

# Operaciones a realizar
x = input("Elige una opción\n")
num1 = int(input("Primer número\n"))
num2 = int(input("Segundo número\n"))
if x == "1":
    print(f"El resultado de sumar {num1} entre {num2} es:", Sumar(num1,num2))
elif x == "2":
    print(f"El resultado de restar {num1} entre {num2} es:", Restar(num1,num2))
elif x == "3":
    print(f"El resultado de dividir {num1} entre {num2} es:", Multiplicar(num1,num2))
elif x == "4":
    try: # Probamos la división
      division = num1/num2 # Almacenamos la división
      print(f"El resultado de dividir {num1} entre {num2} es:", division)
      # Devolvemos el resultado de dividir los dos parametros introducidos por el usuario
    except ZeroDivisionError: # Si la división nos devuelve el error de dividir por 0     
      print ("No se puede dividir por cero") # Devolvemos el siguiente mensaje cuando nos de error de dividir por cero
else:
    print("Opción invalida")