from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, mark, model, door: int, _connect = False):
        # A chamada super() está correta
        super().__init__(mark, model, _connect) 
        self.door = door
    
    def __str__(self):
        # A chamada super().__str__() agora funciona
        base_info = super().__str__() 
        return f"{base_info}, Portas: {self.door}"