# @classmethod
# @staticmethod

# --- @classmethod: Método de classe, recebe a classe como primeiro argumento (cls) e pode acessar atributos e métodos da classe.

class MinhaClasse:
    valor = 10 # Atributo global da classe
    
    def __init__(self, nome) -> None:
        self.nome = nome
        
    # requer uma instância da classe para ser chamado
    def metodo_de_instancia(self):
        return f"Método de instância: {self.nome}"
    
    @classmethod
    def metodo_de_classe(cls):
        return f"Método de classe: {cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático: Não tem acesso a cls ou self"

obj = MinhaClasse(nome="Rocketseat")
print(obj.metodo_de_instancia()) # Precisa de uma instância para acessar o método de instância
print(MinhaClasse.valor) # Não precisa de uma instância para acessar o atributo global da classe
print(MinhaClasse.metodo_de_classe()) # Não precisa de uma instância para acessar o método de classe
print(MinhaClasse.metodo_estatico()) # Não precisa de uma instância para acessar o método estático

class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, config):
        marca, modelo, ano = config.split(", ")
        return cls(marca, modelo, int(ano))

config1 = "Toyota, Corolla, 2020"
config2 = "Honda, Civic, 2026"

carro1 = Carro.criar_carro(config1)
carro2 = Carro.criar_carro(config2)

print(f"Carro 1: {carro1.marca} {carro1.modelo} {carro1.ano}")
print(f"Carro 2: {carro2.marca} {carro2.modelo} {carro2.ano}")


# --- @staticmethod: Método estático, recebe apenas o primeiro argumento (cls) e pode acessar atributos e métodos da classe.

class Matematica:
    
    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(5, 3))