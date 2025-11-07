import os

def calc_tip(value, percent):
    return value * (percent / 100)

def calc_total_account(value, tip):
    return value + tip

def name_program():
    print("===================================")
    print(" Calculadora de Gorjetas ")
    print("===================================\n")

def value_calc():
    os.system("cls")
    name_program()

    try:
        value_account = float(input("Digite o valor da conta: R$ "))
        if value_account <= 0:
            raise ValueError("O valor da conta deve ser maior que zero.")

        value_percent = float(input("Digite a porcentagem da gorjeta (%): "))
        if value_percent < 0:
            raise ValueError("A porcentagem não pode ser negativa.")

    except ValueError as e:
        os.system("cls")
        print(f"⚠️ Erro: {e}\n")
        input("Pressione Enter para tentar novamente...")
        return main()  # volta ao menu

    tip = calc_tip(value_account, value_percent)
    total = calc_total_account(value_account, tip)

    print(f"\n💰 Valor da gorjeta: R${tip:.2f}")
    print(f"💵 Total da conta com gorjeta: R${total:.2f}")
    input("\nPressione Enter para voltar ao menu principal...")

def options_menu(): 
    print("1 - Calcular gorjeta")
    print("2 - Sair\n")
    
def select_option():
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        value_calc()
    elif opcao == 2:
        os.system("cls")
        print("Encerrando o programa...")
    
