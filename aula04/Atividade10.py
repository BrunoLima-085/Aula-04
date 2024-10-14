positivos = 0
negativos = 0

for i in range(10):
    numero = float(input("Insira um número (insira 0 para parar): "))
    
    if numero == 0:
        print("Número 0 inserido. Encerrando o loop.")
        break
    elif numero > 0:
        positivos += 1
    else:
        negativos += 1

print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
