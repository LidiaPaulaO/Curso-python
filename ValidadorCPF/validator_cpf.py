import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def name_program():
    print("======================")
    print("  Validador de CPF   ")
    print("======================")

def options_menu():
    print("Selecione uma opção:")
    print("1 - Validar CPF")
    print("2 - Sair")

def validate_cpf():
    cpf = input("Digite o CPF (Somente números): ").strip()
    cpf = cpf.replace(".", "").replace("-", "")  # opcional: limpa pontuação

    if len(cpf) != 11:
        print("Erro: CPF inválido! Deve conter 11 dígitos.\n")
        return

    if cpf == cpf[0] * len(cpf):
        print("Erro: CPF inválido! Não pode conter todos os dígitos iguais.\n")
        return

    if not cpf.isdigit():
        print("Erro: CPF inválido! Informe apenas números.\n")
        return

    if not calc_check_digit(cpf):
        print("Erro: CPF inválido! Dígitos verificadores incorretos.\n")
    else:
        print("CPF válido!\n")

def calc_check_digit(cpf):
    first_sum = sum(int(cpf[i]) * (10 - i) for i in range(9))
    first_digit = (first_sum * 10) % 11
    if first_digit >= 10:
        first_digit = 0

    second_sum = sum(int(cpf[i]) * (11 - i) for i in range(10))
    second_digit = (second_sum * 10) % 11
    if second_digit >= 10:
        second_digit = 0

    return cpf[-2:] == f"{first_digit}{second_digit}"

def back_pause():
    input("\nPressione Enter para voltar ao menu...")
