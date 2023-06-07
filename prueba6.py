#generador de tabla de multiplicar
num = int(input("ingrese un numero entero: "))
for i in range(1, 11):
    resultado=num*i
    print(f"{num} * {i} = {resultado}")