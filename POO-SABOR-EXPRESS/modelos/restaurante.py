from modelos.avaliacao import Avaliacao


class Restaurante:
    """Classe que representa um restaurante."""

    # Atributo de classe — lista compartilhada por todas as instâncias
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        """Inicializa um novo restaurante."""
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self) -> str:
        """Retorna uma representação legível do restaurante."""
        status = "Aberto" if self._ativo else "Fechado"
        return f"Restaurante: {self._nome} | Categoria: {self._categoria} | Status: {status}"

    # Encapsulamento (propriedades)
    @property
    def ativo(self) -> str:
        """Retorna o status do restaurante em emoji."""
        return "✅" if self._ativo else "❎"

    @property
    def nome(self) -> str:
        """Retorna o nome do restaurante."""
        return self._nome

    @property
    def categoria(self) -> str:
        """Retorna a categoria do restaurante."""
        return self._categoria

    @property
    def media_avaliacoes(self) -> float | None:
        """Retorna a média das avaliações do restaurante ou None se não houver avaliações."""
        if not self._avaliacoes:
            return None
        soma = sum(avaliacao.nota for avaliacao in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)

    def alternar_status(self):
        """Alterna o status do restaurante entre aberto e fechado."""
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        """Lista todos os restaurantes cadastrados."""
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(10)} | Média")
        print("-" * 75)

        for restaurante in cls.restaurantes:
            media = restaurante.media_avaliacoes  # acesso à propriedade
            media_str = f"{media:.1f}" if isinstance(media, (int, float)) else "-"
            print(
                f"{restaurante.nome.ljust(25)} | "
                f"{restaurante.categoria.ljust(25)} | "
                f"{restaurante.ativo.ljust(10)} | "
                f"{media_str}"
            )

    def adicionar_avaliacao(self, cliente: str, nota: int):
        """Adiciona uma nova avaliação ao restaurante."""
        if not isinstance(nota, (int, float)) or nota < 1 or nota > 5:
            raise ValueError("A nota deve ser um número entre 1 e 5.")
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)
