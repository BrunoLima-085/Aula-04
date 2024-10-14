total = 0

for i in range(5):
    preco = float(input(f"Insira o preço do produto {i+1}: "))
    total += preco
    
    if total > 100:
        print("Total ultrapassou 100, aplicando desconto de 10% e interrompendo o loop.")
        total *= 0.9  
        break

print(f"Total a pagar: R$ {total:.2f}")
