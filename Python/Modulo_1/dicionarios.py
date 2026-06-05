# Criando um dicionário de exemplo - DICIONÁRIOS SÃO ESTRUTURAS DE DADOS QUE ARMAZENAM PARES DE CHAVE-VALOR

pessoa = {
    "nome": "Gabriel",
    "idade": 24,
    "cidade": "São Paulo"
}

# Exibindo o dicionário completo
print("Dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Adicionando um novo par chave-valor

pessoa["sobrenome"] = "Bonamichi"
print("Dicionário após adição de sobrenome:", pessoa)

print("Sobrenome:", pessoa["sobrenome"])

# Atualizando um valor existente

pessoa["cidade"] = "Vancouver"
print("Dicionário após atualização da cidade:", pessoa)

# Removendo um par chave-valor usando del

del pessoa["sobrenome"]
print("Dicionário depois de remover o sobrenome:", pessoa)

# Métodos principais: keys(), values() e items()

# Keys(): Retorna uma lista de todas as chaves do dicionário

chave = list(pessoa.keys())
print("Chaves do dicionário:", chave)
print("Primeira chave:", chave[0])

# Values(): Retorna uma lista de todos os valores do dicionário

valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor:", valores[0])

# Items(): Retorna uma lista de tuplas, onde cada tupla é um par chave-valor do dicionário

itens = list(pessoa.items())
print("Itens do dicionário (chave-valor):", itens)
print(f"Primeiro item (TUPLA) (chave-valor): {itens[0]}, chave: {itens[0][0]}, valor: {itens[0][1]}")