from typing import Any

def meu_decorador(func):
    def wrapper():
        print("Antes de chamar a função.")
        func()
        print("Depois de chamar a função.")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada.")

minha_funcao()

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> Any:
        print("Antes de chamar a função (Decorador de Classe).")
        self.func()
        print("Depois de chamar a função (Decorador de Classe).")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda função foi chamada.")

segunda_funcao()
    