def adicionar_contato(nome, telefone, email, favorito):
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    contatos.append(contato)
    print(f"O contato {nome} foi adicionado com sucesso!")
    return

def listar_contatos(contatos):
    if contatos == []:
        print("Nenhum contato encontrado.")
        
    else:
        for indice, contato in enumerate(contatos, start=1):
            favorito = " (FAV)" if contato["favorito"] == 's' else " "
            print(f"{indice}. {contato['nome']} - {contato['telefone']} - {contato['email']}{favorito}")
    return

def editar_contato(indice_contato, nome, telefone, email):
    indice_contato_ajustado = int(indice_contato) - 1
    
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        
        print("Selecione o que voce quer editar:")
        print("1. Nome")
        print("2. Telefone")
        print("3. Email")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o novo nome: ")
            
        elif escolha == '2':
            telefone = input("Digite o novo telefone: ")
            
        elif escolha == '3':
            email = input("Digite o novo email: ")
            
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
        
        contatos[indice_contato_ajustado]["nome"] = nome
        contatos[indice_contato_ajustado]["telefone"] = telefone
        contatos[indice_contato_ajustado]["email"] = email
        print(f"Contato {indice_contato} atualizado com sucesso!")
    
    else:
        print("Índice de contato inválido.")
    return

def marcar_desmarcar_favorito(indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    listar_contatos(contatos)
    
    if 0 <= indice_contato_ajustado < len(contatos):
        contato = contatos[indice_contato_ajustado]
        contato["favorito"] = "n" if contato["favorito"] == "s" else "s"
        print(f"Contato {contato['nome']} foi marcado como {'favorito' if contato['favorito'] == 's' else 'não favorito'} com sucesso!")
        
    else:
        print("Índice de contato inválido.")

def lista_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato["favorito"] == "s"]
    listar_contatos(favoritos)

def apagar_contato(indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    
    if 0 <= indice_contato_ajustado < len(contatos):
        contato = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato['nome']} foi apagado com sucesso!")
        
    else:
        print("Índice de contato inválido.")

contatos = []

while True:
    print("\n-----S U A  A G E N D A-----\n")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato existente")
    print("4. Marcar ou desmarcar contato como favorito")
    print("5. Mostrar lista de contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")
    print("\n-----------------------------\n")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        print("Adicionando contato")
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato:: ")
        email = input("Digite o email do contato: ")
        favorito = input("O contato é favorito? (s/n): ").lower()
        adicionar_contato(nome, telefone, email, favorito)
    
    elif escolha == '2':
        print("Listando contatos")
        listar_contatos(contatos)
    
    elif escolha == '3':
        print("Editando contato existente")
        listar_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja editar: ")
        editar_contato(indice_contato, nome, telefone, email)
    
    elif escolha == '4':
        print("Marcando ou desmarcando contato como favorito")
        listar_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja marcar ou desmarcar como favorito: ")
        marcar_desmarcar_favorito(indice_contato)
    
    elif escolha == '5':
        print("Mostrando lista de contatos favoritos")
        lista_favoritos(contatos)

    elif escolha == '6':
        print("Apagando contato")
        listar_contatos(contatos)
        indice_contato = input("Digite o indice do contato que deseja apagar: ")
        apagar_contato(indice_contato)

    elif escolha == '7':
        print("Saindo da agenda...")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    


