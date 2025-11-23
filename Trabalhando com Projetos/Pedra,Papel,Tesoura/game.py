import random
import os
play = ["Pedra", "Papel", "Tesoura"]
roles = {
    "Pedra": "Tesoura",
    "Tesoura": "Papel",
    "Papel": "Pedra"
}

def back_pause():
    input("\nPressione Enter para voltar ao menu...")
    os.system("cls" if os.name == "nt" else "clear")

def name_program():
    print("=============================")
    print("   Pedra, Papel e Tesoura   ")
    print("=============================")

def options_menu():
    print("1 - Jogar")
    print("2 - Sair")

def options_game():
    print("=============================")
    print("Selecione sua jogada:")
    print("=============================")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    

def game():
    options_game()
    try:
        played_user = int(input("Digite sua jogada:"))
        if played_user not in [1,2,3]:
            print("Opção invalida!")
            back_pause()
            return
    except ValueError:
        print("Apenas numeros são permitidos!")
        return
    played_user = play[played_user - 1]
    played_computer = random.choice(play)
    print(f"Voce jogou: {played_user}")
    print(f"O computador jogou:{played_computer}")
    if played_user == played_computer:
        print("Empate!")
    elif roles[played_user] == played_computer:
        print("Voce venceu!")
    else:
        print("Computador venceu!")
    back_pause()
