# Declaração da Lista

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, 3.14, False]

print("Minha lista de exemplo:", minha_lista)

# Exibindo elementos individualmente

print("Primeiro elemento da lista[0]:", minha_lista[0])
print("Quarto elemento da lista[3]:", minha_lista[3])

# Fatiando a lista

print("Fatiando a lista[1:7]:", minha_lista[1:7])
print("Do inicio até tal elemento[:6]:", minha_lista[:6])
print("Do elemento 6 em diante[5:]:", minha_lista[5:])

# Ultimo elemento sem saber o tamanho da lista

print("Ultimo elemento da lista[-1]:", minha_lista[-1])

# Alterando o primeiro elemento da lista

minha_lista[0] = "Python"
print("Minha lista após alteração do primeiro elemento:", minha_lista)

# Métodos de lista

# Método append() - Adiciona um elemento ao final da lista

minha_lista.append(6)
print("Minha lista com append:", minha_lista)

# Método index() - Retornar o índice do elemento encontrado

indice = minha_lista.index(6)
print("Índice do elemento 6:", indice)

# Método insert() - Adiciona um elemento em um índice específico

minha_lista.insert(2, 10)
print("Minha lista com insert:", minha_lista)

# Método pop() - Remove o último elemento da lista ou um elemento específico por índice e retorna o elemento removido

elemento_removido = minha_lista.pop(7)
print("Elemento removido:", elemento_removido)
print("Minha lista após pop:", minha_lista)

# Método remove() - Remove a primeira ocorrência do elemento especificado

minha_lista.remove(10)
print("Minha lista com remove:", minha_lista)

# Método sort() - Ordena os elementos da lista (apenas para elementos do mesmo tipo)

minha_lista2 = [5, 2, 9, 1, 3, 112, 10, 10, 10, 10, 1, 1]
print("Minha lista de números antes do sort:", minha_lista2)

minha_lista2.sort()
print("Minha lista com sort:", minha_lista2)