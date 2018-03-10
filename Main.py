import sys
import os
import ClienteClass

lista_cliente = []
nome_arquivo = "clientes_cadastrados.txt"

############# RETORNA O ULTIMO ID CADASTRADO ##############
def retorna_ultimo_id():
    return len(lista_cliente)

############# CADASTRANDO OS CLIENTES ##############
def cadastrar_cliente():
    cliente = ClienteClass.Cliente()

    id = retorna_ultimo_id()
    nome = input("\nDigite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o email do cliente: ")

    if(cliente.setId(id) and cliente.setNome(nome) and cliente.setIdade(idade) and cliente.setEmail(email)):
        lista_cliente.append(cliente)
        print("Cliente cadastrado com sucesso")
    else:
        print("O cliente nao foi cadastro")

    print("\n")

############# LISTANDO OS CLIENTES ##############
def visualizar_clientes():
    print("\n" * 5)
    for i in lista_cliente:
        print("ID: " + str(i.getId()), end="\t|\t")
        print("Cliente: " + i.getNome(), end="\t|\t")
        print("Idade: " + i.getIdade(), end="\t|\t")
        print("Email: " + i.getEmail(), end="\n")

############# DELETANDO O CLIENTE ##############
def deletar_cliente():
    id_cliente = input("Digite o ID do cliente que deseja deletar: ")

    for cliente in lista_cliente:
        if(cliente.getId() == id_cliente):
            lista_cliente.remove(cliente)

############# EDITANDO O CLIENTE ##############
def editar_cliente():
    id_cliente = input("Digite o ID do cliente que deseja editar: ")

    for cliente in lista_cliente:
        if cliente.getId() == id_cliente:
            if input("Deseja editar o nome? S/N ") == "S": nome = input("\nDigite o nome do cliente: ")
            else: nome = cliente.getNome()

            if input("Deseja editar a idade? S/N ") == "S": idade = input("Digite a idade do cliente: ")
            else: idade = cliente.getIdade()

            if input("Deseja editar o email? S/N ") == "S": email = input("Digite o email do cliente: ")
            else: email = cliente.getEmail()

            if cliente.setNome(nome) and cliente.setIdade(idade) and cliente.setEmail(email):
                print("Cliente editado com sucesso")
            else:
                print("O cliente nao foi editado")

############# SALVANDO AS ALTERACOES ##############
def rotina_saida():
    clientes_cadastados = open(nome_arquivo, "w+")

    for cliente in lista_cliente:
        clientes_cadastados.write(str(cliente.getId()) + "," + cliente.getNome() + "," + cliente.getIdade() + "," + cliente.getEmail() + "\n")

    clientes_cadastados.close()

############# PREENCHENDO A LISTA ##############
def inicializar():
    if(os.path.isfile(nome_arquivo)):
        clientes_cadastados = open(nome_arquivo, "r")

        for linha in clientes_cadastados.readlines():
            linha_array = linha.split(",")

            cliente = ClienteClass.Cliente()


            cliente.setId(linha_array[0])
            cliente.setNome(linha_array[1])
            cliente.setIdade(linha_array[2])
            cliente.setEmail(linha_array[3])
            lista_cliente.append(cliente)

        clientes_cadastados.close()


############# MAIN ##############
opcao = 1

inicializar()

############# MENU ##############
while(opcao != 0):
    print("Bem vindo ao cadastro de clientes\nSelecione uma opçao abaixo:\n")
    print("[1] - Cadastrar cliente")
    print("[2] - Visualizar clientes cadastrados")
    print("[3] - Deletar cliente")
    print("[4] - Editar cliente")
    print("[0] - Sair")

    opcao = int(sys.stdin.readline())

    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        visualizar_clientes()
    elif opcao == 3:
        deletar_cliente()
    elif opcao == 4:
        editar_cliente()
    elif opcao == 0:
        rotina_saida()
    else:
        print("Opção invalida")


