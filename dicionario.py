elenco = {"renato": "600.000,00", "yuri": "1.000.000,00", "murilo": "80.000,00"}
while True:
    jogador = input("Digite o nome do jogador ou fim para terminar:")
    if jogador.lower() == "fim":
        break
    elif jogador in elenco:
        print(f"Preço: R$ {elenco[jogador]}")
    else:
        print("Jogador não está no elenco.")
