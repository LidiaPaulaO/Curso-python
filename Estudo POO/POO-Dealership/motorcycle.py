from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, mark, model, type: str, _connect = False):
        super().__init__(mark, model, _connect)
        self.type = type
        
    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}, Tipo: {self.type}"