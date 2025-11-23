from game import *
import os
def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        name_program()
        options_menu()

        try:
            option = int(input("Digite uma opção: ").strip())
        except ValueError:
            print("Por favor, digite um número válido.")

        if option == 1:
            os.system("cls" if os.name == "nt" else "clear")
            name_program()
            game()
        elif option == 2:
            os.system("cls" if os.name == "nt" else "clear")
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            back_pause()

if __name__ == "__main__":
    main()