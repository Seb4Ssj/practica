imc = lambda peso, altura: peso/altura**2
resultado = imc(69, 1.75)


if resultado<18.5:
    print(f"Tu IMC es de {resultado} y te encuentras delgado")
elif resultado<24.9:
    print(f"Tu IMC es de {resultado} y te encuentras en un peso adecuado")
elif resultado<29.9:
    print(f"Tu IMC es de {resultado} y te encuentras con sobrepeso")
elif resultado<34.9:
    print(f"Tu IMC es de {resultado} y te encuentras con obesidad grado 1")
elif resultado<39.9:
    print(f"Tu IMC es de {resultado} y te encuentras con obesidad grado 2")
else:
    print(f"Tu IMC es de {resultado} y te encuentras con obesidad grado 3 o obesidad morbida")