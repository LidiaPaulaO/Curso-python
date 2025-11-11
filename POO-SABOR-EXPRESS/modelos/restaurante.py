class Restaurante:
    # 1. Atributo de Classe
    restaurantes = []
    
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        # Atributo protegido, acessado pelo getter/setter
        self._ativo = False 
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        status = "Aberto" if self._ativo else "Fechado"
        return f"Restaurante: {self.nome} | Categoria: {self.categoria} | Status: {status}"
    
    @classmethod # Boa prática: Indica que o método usa dados da classe
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        print("-" * 59)
        for restaurante in cls.restaurantes:
            # 3. Chamando a propriedade 'ativo' (que usa o getter)
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}")
    
    @property
    def ativo(self):
        # 2. Corrigido para retornar a string (o ícone), e não um set
        return "✅" if self._ativo else "❎"

# Instâncias
restaurante_praca = Restaurante("Sabor na Praça", "Comida Caseira")
restaurante_pizza = Restaurante("La casa della Pizza", "Pizza")

Restaurante.listar_restaurantes()