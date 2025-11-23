from modelos.restaurante import Restaurante

def main():
    """Função principal do programa."""

    # Criação de instâncias de restaurantes
    restaurante1 = Restaurante("Sabor Caseiro", "Comida Caseira")
    restaurante2 = Restaurante("Sushi Express", "Comida Japonesa")
    restaurante3 = Restaurante("Tacos Lokos", "Comida Mexicana")

    # Alterna o status do primeiro restaurante
    restaurante1.alternar_status()

    # Adiciona avaliações
    # restaurante1.adicionar_avaliacao("Lidia", 10)
    # restaurante1.adicionar_avaliacao("Paula", 8)
    # restaurante2.adicionar_avaliacao("Carlos", 7)
    # restaurante3.adicionar_avaliacao("Fernanda", 9)

    # Lista todos os restaurantes
    Restaurante.listar_restaurantes()


# Ponto de entrada do programa
if __name__ == "__main__":
    main()
