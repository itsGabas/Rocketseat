# Exemplo

def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudacao:")
saudacao("Gabriel")
saudacao("Ana Luiza")
saudacao("Sofia")

# Função com retorno

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando a função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da função quadrado:", resultado_quadrado)

# Função com múltiplos parâmetros

def soma(num1, num2):
    resultado = num1 + num2
    return resultado

print("\nChamando a função soma:")
resultado_soma = soma(20, 50)
print("A soma do numero 20 e numero 50 é:", resultado_soma)