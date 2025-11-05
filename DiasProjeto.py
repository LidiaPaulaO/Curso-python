AtividadeA = int(input("Digite os dias para a Atividade A: \n"))
AtividadeB = int(input("Digite os dias para a Atividade B: \n"))
AtividadeC = int(input("Digite os dias para a Atividade C: \n"))
if AtividadeA < 0 or AtividadeB < 0 or AtividadeC < 0:
    print("Erro: os dias não pode ser menor que 0")
else:
    tempoTotal = AtividadeA + AtividadeB + AtividadeC
    print(f"O projeto ira levar {tempoTotal} dias")