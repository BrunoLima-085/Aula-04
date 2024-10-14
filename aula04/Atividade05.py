positivos = 0
negativos = 0

numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)] 

for numero in numeros:
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")