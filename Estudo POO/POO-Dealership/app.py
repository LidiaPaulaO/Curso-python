from car import Car
from motorcycle import Motorcycle
from vehicle import Vehicle # Opcional: Para testar a classe base

def main():
    
    # 🚗 Instâncias de Carro 
    
    carro1 = Car("Volkswagen", "Gol", 2, _connect=True) 
    carro2 = Car("Peugeot", "206", 4)
    
    
    # 🏍️ Instâncias de Moto 
    
    # Moto 1: Tipo Esportiva, Desconectada (Valor padrão False)
    moto1 = Motorcycle("Kawasaki", "Ninja 400", type="Esportiva")
    
    # Moto 2: Tipo Urbana, Conectada (True)
    moto2 = Motorcycle("Honda", "CG 160", type="Urbana", _connect=True)
    
    print("## 🚗 Informações dos Carros")
    print(carro1)
    print(carro2)
    
    print("\n## 🏍️ Informações das Motos")
    print(moto1)
    print(moto2)

if __name__ == "__main__":
    main()