peso = float(input("Insira seu peso em KG: "))
altura = float(input("Insira sua altura em metros: "))
imc = peso /altura**2
print(round(imc,2))

if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30.0 and imc<= 34.9:
    print("Obesidade grau 1")
else:
    print("Obesidade graus 2")
