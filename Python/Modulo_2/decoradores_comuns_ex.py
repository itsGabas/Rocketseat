class Animal:
    def __init__(self, nome, tipo, raça) -> None:
        self.nome = nome
        self.tipo = tipo
        self.raça = raça

    @classmethod
    def criar_animal(cls, config):
        nome, tipo, raça = config.split(", ")
        return cls(nome, tipo, raça)

animal1 = Animal.criar_animal("Rex, Cachorro, Labrador")
animal2 = Animal.criar_animal("Miau, Gato, Siamês")

print(f"Animal 1: {animal1.nome} - {animal1.tipo} - {animal1.raça}")
print(f"Animal 2: {animal2.nome} - {animal2.tipo} - {animal2.raça}")

class Pessoa:
    def __init__(self, nome, idade, sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    
    @classmethod
    def criar_pessoa(cls, config):
        nome, idade, sexo = config.split(",")
        return cls(nome, int(idade), sexo)

pessoa1 = Pessoa.criar_pessoa("Sofia, 18, Feminino")
pessoa2 = Pessoa.criar_pessoa("Gabriel, 24, Masculino")

print(f"Pessoa 1: {pessoa1.nome} - {pessoa1.idade} - {pessoa1.sexo}")
print(f"Pessoa 2: {pessoa2.nome} - {pessoa2.idade} - {pessoa2.sexo}")

class Escritorio:
    
    def __init__(self, func, cargo, salario) -> None:
        self.func = func
        self.cargo = cargo
        self.salario = salario
        
    @classmethod
    def criar_funcionario(cls, config):
        func, cargo, salario = config.split(",")
        return cls(func, cargo, float(salario))
    
func1 = Escritorio.criar_funcionario("Ana, Gerente, 5000")
func2 = Escritorio.criar_funcionario("Carlos, Analista, 3000")
func3 = Escritorio.criar_funcionario("Mariana, Desenvolvedora, 4000")

print(f"Funcionario 1: {func1.func} - {func1.cargo} - {func1.salario}")
print(f"Funcionario 2: {func2.func} - {func2.cargo} - {func2.salario}")
print(f"Funcionario 3: {func3.func} - {func3.cargo} - {func3.salario}")

class Cidade:
    
    def __init__(self, nome, pais, populacao) -> None:
        self.nome = nome
        self.pais = pais
        self.populacao = populacao
        
    @classmethod
    def criar_cidade(cls, config):
        nome, pais, populacao = config.split(",")
        return cls(nome, pais, int(populacao))

cidade1 = Cidade.criar_cidade("São Paulo, Brasil, 12000000")
cidade2 = Cidade.criar_cidade("Rio de Janeiro, Brasil, 13000000")
cidade3 = Cidade.criar_cidade("Brasília, Brasil, 3000000")

print(f"Cidade 1: {cidade1.nome} - {cidade1.pais} - {cidade1.populacao}")
print(f"Cidade 2: {cidade2.nome} - {cidade2.pais} - {cidade2.populacao}")
print(f"Cidade 3: {cidade3.nome} - {cidade3.pais} - {cidade3.populacao}")