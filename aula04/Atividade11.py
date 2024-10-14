for num in range(1, 31):
    if num > 20:
        print("Número maior que 20 encontrado. Encerrando o loop.")
        break
    if num % 5 == 0:
        print(f"{num} é múltiplo de 5.")
    else:
        print(num)
