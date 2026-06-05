# Criando uma tupla de exemplo - TUPLAS SÃO IMUTÁVEIS, OU SEJA, NÃO PODEM SER ALTERADAS APÓS A CRIAÇÃO

minha_tupla = (1, 2, 2, 3, 4)
print("Minha tupla de exemplo:", minha_tupla)

# Acessando elementos da tupla

print("Primeiro elemento da tupla[0]:", minha_tupla[0])
print("Terceiro elemento da tupla[2]:", minha_tupla[2])
print("Último elemento da tupla[-1]:", minha_tupla[-1])

# Método count() - Retorna o número de vezes que um elemento aparece na tupla

contador = minha_tupla.count(2)
print("Número de vezes que o elemento 2 aparece na tupla:", contador)

# Método index() - Retorna o índice da primeira ocorrência do elemento especificado

indice = minha_tupla.index(3)
print("Índice do elemento 3 na tupla:", indice)

print("Tipo da tupla:", type(minha_tupla))
