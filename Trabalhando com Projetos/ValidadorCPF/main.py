from  validator_cpf import *
def main():
    while True:
        clear_screen()
        name_program()
        options_menu()

        try:
            option = int(input("Digite uma opção: ").strip())
        except ValueError:
            print("Por favor, digite um número válido.")
            back_pause()
            continue

        if option == 1:
            clear_screen()
            name_program()
            validate_cpf()
            back_pause()
        elif option == 2:
            clear_screen()
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            back_pause()

if __name__ == "__main__":
    main()