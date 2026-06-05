nome = "Gabriel Bonamichi"

print(f"Contando caracteres: 'COUNT': {nome.count('a')}")

print(f"Verificando local da letra: 'FIND': {nome.find('i')}")

print(f"Transformando em bytes: 'ENCODE': {nome.encode()}")

print(f"Descodificando: 'DECODE': {nome.encode().decode()}")

print(f"Colocando outra letra: 'REPLACE': {nome.replace('a', 'b')}")

print(f"Colocando tudo em maiúsculo: 'UPPER': {nome.upper()}")

print(f"Colocando tudo em minúsculo: 'LOWER': {nome.lower()}")

print(f"Colocando um caractere entre cada letra: 'JOIN': {'-'.join(nome)}")

print(f"Separando o nome: 'SPLIT': {nome.split()}")

print(f"Removendo alguma letra NO COMEÇO OU NO FIM: 'STRIP': {nome.strip('G')}")

print(f"Removendo alguma letra NO COMEÇO: 'LSTRIP': {nome.lstrip('G')}")

print(f"Removendo alguma letra NO FIM: 'RSTRIP': {nome.rstrip('i')}")

print("Verificando se o nome começa com 'G': 'STARTSWITH':", nome.startswith('G'))

print("Verificando se o nome termina com 'i': 'ENDSWITH':", nome.endswith('i'))

print("Verificando se existe tal termo no nome: 'IN':", 'ch' in nome)

print("Verificando se existe tal termo no nome: 'NOT IN':", 'ch' not in nome)