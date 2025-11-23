class Vehicle:
    def __init__(self, mark: str, model: str, _connect: bool = False):
        if not isinstance(mark, str) or not mark.strip():
            raise ValueError("Mark cannot be empty")
        
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Model cannot be empty")
        
        self.mark = mark.title()
        self.model = model.title()
        self._connect = _connect 
    
    def __str__(self) -> str:
        # AGORA, self._connect existe
        status = "Connected" if self._connect else "Disconnected" 
        return f"{self.mark} | {self.model} | {status}"

    # Opcional, para demonstrar que o atributo é acessível
    def is_connected(self):
        return self._connect