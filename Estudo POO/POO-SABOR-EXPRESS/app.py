from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Criação de instâncias de restaurantes
restaurante1 = Restaurante("Sabor Caseiro", "Comida Caseira")
restaurante2 = Restaurante("Sushi Express", "Comida Japonesa")
restaurante3 = Restaurante("Tacos Lokos", "Comida Mexicana")

bebida_suco = Bebida("Suco Melancia",5.0, "grande")
prato_pao = Prato("Paozinho",2.0,"O melhor paozinho")

def main():


pass
# Ponto de entrada do programa
if __name__ == "__main__":
    main()
