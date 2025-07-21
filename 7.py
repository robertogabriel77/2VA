frase = str(input("insira uma frase: "))

vogais = "aeiou"
contador=0

for letras in frase.lower():
    if letras in vogais:
        contador+=1

print(f"a frase contém {contador} vogais.")
