print("FOR utilizando lista")

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print("Elemento da lista:", elemento)
    
print("\nFOR utilizando tupla")
    
tupla = (10, 20, 30, 40, 50)

for elemento in tupla:
    print("Elemento da tupla:", elemento)

pessoa = {
    "nome": "Gabriel",
    "idade": 24,
    "cidade": "São Paulo"
}

print("\nFOR utilizando dicionário - CHAVES")

for chave in pessoa.keys():
    print("Chave:", chave)

print("\nFOR utilizando dicionário - VALORES")

for valor in pessoa.values():
    print("Valor:", valor)

print("\nFOR utilizando dicionário - ITENS (CHAVE-VALOR)")

for item in pessoa.items():
    print("Item:", item)

print("\nFOR utilizando dicionário - ITENS (CHAVE-VALOR) DESESTRUTURADOS")

for chave, valor in pessoa.items():
    print(f"Chave: {chave}, Valor: {valor}")

# Range - FOR utilizando range para gerar uma sequência de números

for numero in range(0, 5):
    print("\nNúmero gerado pelo range:", numero)

# Utilizando range com len

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
    print("Indice:", indice)
    print("Elemento da lista:", lista[indice])
    if indice == 3:
        lista[indice] = 10
        print("\nLista após modificação:", lista)

# Função enumerate() - FOR utilizando enumerate para obter índice e valor

lista_enumerate = ['a', 'b', 'c']
for indice, valor in enumerate(lista_enumerate):
    print(f"\n{indice}: {valor}")
    if indice == 1:
        print("\nIndice 1")