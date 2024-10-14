for num in range(1, 21):
    if num == 15:
        print("Número 15 encontrado. Encerrando o loop.")
        break
    elif num % 2 == 0:
        print(f"{num} é par.")
    else:
        print(f"{num} é ímpar.")
