class Avaliacao:
    """Classe que representa uma avaliação de um restaurante."""

    def __init__(self, cliente: str, nota: int):
        """
        Inicializa uma avaliação.

        Args:
            cliente (str): Nome do cliente que fez a avaliação.
            nota (int): Nota atribuída (ex: de 0 a 10).
        """
        self._cliente = cliente
        # Garante que a nota está entre 0 e 10
        self._nota = self._validar_nota(nota)

    def __str__(self) -> str:
        """Retorna uma representação textual da avaliação."""
        return f"{self._cliente} - Nota: {self._nota}"

    @property
    def cliente(self) -> str:
        """Retorna o nome do cliente."""
        return self._cliente

    @property
    def nota(self) -> int:
        """Retorna a nota atribuída pelo cliente."""
        return self._nota

    def _validar_nota(self, nota: int) -> int:
        """Garante que a nota seja um número entre 0 e 10."""
        if not (0 <= nota <= 10):
            raise ValueError("A nota deve estar entre 0 e 10.")
        return nota
