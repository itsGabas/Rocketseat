import random

class Personagem:
    """ Classe para criar os personagens. """
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    @property    
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @property
    def nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.nome}\nVida: {self.vida}\nNivel: {self.nivel}"

    def atacar(self, alvo):
        # Dano randomico baseado no nível do personagem
        dano = random.randint(self.nivel * 2, self.nivel * 6)
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel) # Cria o Objeto, no caso, cria o Heroi, utilizando o construtor da classe mãe (Personagem)
        self.__habilidade = habilidade
        
    @property
    def habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.habilidade}"
    
    def especial(self, alvo):
        dano = random.randint(self.nivel * 5, self.nivel * 10)
        alvo.receber_dano(dano)
        print(f"{self.habilidade.upper()}!!!")
        print(f"\n{self.nome} usou {self.habilidade} causando {dano} de dano em {alvo.nome}!")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo, habilidade):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        self.__habilidade = habilidade
    
    @property
    def habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.tipo}\nHabilidade: {self.habilidade}"
    
    @property
    def tipo(self):
        return self.__tipo
    
    def especial(self, alvo):
        dano = random.randint(self.nivel * 6, self.nivel * 11)
        alvo.receber_dano(dano)
        print(f"{self.habilidade.upper()}!!!")
        print(f"\n{self.nome} usou {self.habilidade} causando {dano} de dano em {alvo.nome}!")

class Jogo:
    """ Classe orquestradora do jogo. """
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Gabriel", vida=100, nivel=5, habilidade="Fireball")
        self.inimigo = Inimigo(nome="Orc", vida=100, nivel=5, tipo="Shaman", habilidade="Lightning Bolt")
    
    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos """
        print("Batalha Iniciada!")
        
        while self.heroi.vida > 0 and self.inimigo.vida > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(f"\n{self.inimigo.exibir_detalhes()}")
            
            input("\nPressione Enter para atacar...")
            escolha = input("\nEscolha o ataque (1 - Spell, 2 - Fireball): ")
            
            if escolha == "1":
                self.heroi.atacar(self.inimigo)
                if self.inimigo.vida <= 0:
                    break
                self.inimigo.atacar(self.heroi)
            
            elif escolha == "2":
                self.heroi.especial(self.inimigo)
                if self.inimigo.vida <= 0:
                    break
                self.inimigo.especial(self.heroi)
            
            else:
                print(f"\nHabilidade não disponível. {self.heroi.nome } errou o ataque.")
            
        
        if self.heroi.vida > 0:
            print("\n O INIMIGO FOI DERROTADO!!!")
            print("\nParabéns! Você venceu a batalha!")
            print("\n XP + 10")
        
        elif self.inimigo.vida <= 0 and self.heroi.vida <= 0:
            print("\n O HERÓI FOI DERROTADO!!! MAS O INIMIGO TAMBÉM...")
            print("\nXP + 0")
        
        else:
            print("\nGame Over! O inimigo venceu a batalha.")
            print("\n XP - 5")
            
# Criar instância do jogo e iniciar batalha
jogo = Jogo()
jogo.iniciar_batalha()