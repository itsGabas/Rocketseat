# POO

# Classe - é um molde para criar objetos. Ela define as características e comportamentos que os objetos criados a partir dela terão.

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Obejtos - são instâncias de uma classe. Eles possuem as características e comportamentos definidos pela classe.

pessoa1 = Pessoa("Gabriel", 24)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Sofia", 19)
mensagem = pessoa2.saudacao()
print(mensagem)

# Vantagens da POO:
# 1. Reutilização de código: A POO permite criar classes reutilizáveis.
# 2. Organização: A POO ajuda a organizar o código em torno de objetos e suas interações.
# 3. Encapsulamento: A POO permite ocultar os detalhes internos de um objeto e expor apenas o necessário.
# 4. Herança: A POO permite criar novas classes a partir de classes existentes
# 5. Polimorfismo: A POO permite que objetos de diferentes classes sejam tratados de maneira uniforme.