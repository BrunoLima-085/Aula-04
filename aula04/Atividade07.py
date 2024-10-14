palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
cont_vogais = 0

for letra in palavra:
    if letra in vogais:
        cont_vogais += 1

print(f"O número de vogais na palavra '{palavra}' é: {cont_vogais}")