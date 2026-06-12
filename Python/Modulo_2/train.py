import random

class Transporte:
    def __init__(self, tipo, modo, capacidade):
        self.__tipo = tipo
        self.__modo = modo
        self.__capacidade = capacidade
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def modo(self):
        return self.__modo
    
    @property
    def capacidade(self):
        return self.__capacidade
    
class Carro(Transporte):
    def __init__(self, tipo, modo, capacidade, marca, modelo):
        super().__init__(tipo, modo, capacidade)
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    def velocidade(self):
        return random.randint(50, 420) # Velocidade aleatória para transporte de quatro rodas

carro1 = Carro(tipo="Automóvel", modo="Quatro Rodas", capacidade=5, marca="Audi", modelo="RS7")
carro2 = Carro(tipo="Automóvel", modo="Quatro Rodas", capacidade=5, marca="Nissan", modelo="GTR")
carro3 = Carro(tipo="Automóvel", modo="Quatro Rodas", capacidade=5, marca="Porsche", modelo="911 Turbo S")
carro4 = Carro(tipo="Automóvel", modo="Quatro Rodas", capacidade=5, marca="Ferrari", modelo="F8 Tributo")
carro5 = Carro(tipo="Automóvel", modo="Quatro Rodas", capacidade=5, marca="Lamborghini", modelo="Huracán EVO")

class Moto(Transporte):
    def __init__(self, tipo, modo, capacidade, marca, modelo):
        super().__init__(tipo, modo, capacidade)
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    def velocidade(self):
        return random.randint(50, 350) # Velocidade aleatória para transporte de duas rodas

moto1 = Moto(tipo="Motocicleta", modo="Duas Rodas", capacidade=2, marca="Triumph", modelo="Rocket 3")
moto2 = Moto(tipo="Motocicleta", modo="Duas Rodas", capacidade=2, marca="Ducati", modelo="Panigale V4")
moto3 = Moto(tipo="Motocicleta", modo="Duas Rodas", capacidade=2, marca="Yamaha", modelo="YZF-R1")
moto4 = Moto(tipo="Motocicleta", modo="Duas Rodas", capacidade=2, marca="Kawasaki", modelo="Ninja H2")
moto5 = Moto(tipo="Motocicleta", modo="Duas Rodas", capacidade=2, marca="Suzuki", modelo="GSX-R1000")

class Aviao(Transporte):
    def __init__(self, tipo, modo, capacidade, marca, modelo):
        super().__init__(tipo, modo, capacidade)
        self.__marca = marca
        self.__modelo = modelo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    def velocidade(self):
        return random.randint(50, 1200) # Velocidade aleatória para transporte aéreo

aviao1 = Aviao(tipo="Avião", modo="Aéreo", capacidade=100, marca="Boeing", modelo="747")
aviao2 = Aviao(tipo="Avião", modo="Aéreo", capacidade=1, marca="Militar", modelo="F-22 Raptor")
aviao3 = Aviao(tipo="Avião", modo="Aéreo", capacidade=1, marca="Militar", modelo="F-35 Lightning II")
aviao4 = Aviao(tipo="Avião", modo="Aéreo", capacidade=1, marca="Militar", modelo="Su-57")
aviao5 = Aviao(tipo="Avião", modo="Aéreo", capacidade=1, marca="Militar", modelo="J-20")

class Corrida:
    def __init__(self) -> None:
        self.participantes = []
    
    def add_participante(self, *transportes):
        self.participantes.extend(transportes)
    
    def sortear_participantes(self):
        if len(self.participantes) < 2:
            print("É necessário pelo menos 2 participantes para sortear.")
            return
        
        transporte1, transporte2, transporte3, transporte4 = random.sample(self.participantes, 4)
        self.drag_race(transporte1, transporte2, transporte3, transporte4)
    
    def drag_race(self, transporte1, transporte2, transporte3, transporte4):
        vel1 = transporte1.velocidade()
        vel2 = transporte2.velocidade()
        vel3 = transporte3.velocidade()
        vel4 = transporte4.velocidade()
        
        print(f"Corrida entre {transporte1.marca} {transporte1.modelo} / {transporte2.marca} {transporte2.modelo} / {transporte3.marca} {transporte3.modelo} / {transporte4.marca} {transporte4.modelo}!!!")
        print(f"{transporte1.marca} {transporte1.modelo} velocidade: {vel1} km/h")
        print(f"{transporte2.marca} {transporte2.modelo} velocidade: {vel2} km/h")
        print(f"{transporte3.marca} {transporte3.modelo} velocidade: {vel3} km/h")
        print(f"{transporte4.marca} {transporte4.modelo} velocidade: {vel4} km/h")

        velocidades = {
            transporte1: vel1,
            transporte2: vel2,
            transporte3: vel3,
            transporte4: vel4
        }

        maior_vel = max(velocidades.values())
        vencedores = [t for t, v in velocidades.items() if v == maior_vel]

        if len(vencedores) > 1:
            nomes = ", ".join(f"{t.marca} {t.modelo}" for t in vencedores)
            print(f"\nEmpate entre: {nomes} com {maior_vel} km/h!")
            
        else:
            vencedor = vencedores[0]
            print(f"\nVENCEDOR: {vencedor.marca} {vencedor.modelo} com {maior_vel} km/h!")
            
corrida1 = Corrida()

corrida1.add_participante(carro1, carro2, carro3, carro4, carro5,
                          moto1, moto2, moto3, moto4, moto5,
                          aviao1, aviao2, aviao3, aviao4, aviao5)

corrida1.sortear_participantes()