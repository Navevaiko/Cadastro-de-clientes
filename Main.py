import sys
import os
import time
import re
import ClienteClass

lista_cliente = []
nome_arquivo = "clientes_cadastrados.txt"

def clear():
    print("\n"*100)

############# RETORNA O ULTIMO ID CADASTRADO ##############
def retorna_ultimo_id():
    if len(lista_cliente) == 1:
        return lista_cliente[len(lista_cliente)-1].getId() + 1
    else:
        return 1
    

############# CADASTRANDO OS CLIENTES ##############
def cadastrar_cliente():
    cliente = ClienteClass.Cliente()

    id = retorna_ultimo_id()
    nome = input("\nDigite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o email do cliente: ")

    try:
        if(cliente.setId(id) and cliente.setNome(nome) and cliente.setIdade(idade) and cliente.setEmail(email)):
            lista_cliente.append(cliente)
            print("Cliente cadastrado com sucesso")
        else:
            print("O cliente nao foi cadastro")
    except ValueError:
        print("Cliente não cadastrado, insira os valores corretamente")

    time.sleep(1)
    clear()

    print("\n")
    salvar_alteracoes()

############# LISTANDO OS CLIENTES ##############
def visualizar_clientes():
    print("\n" * 5)
    if len(lista_cliente):
        for i in lista_cliente:
            print("ID: " + str(i.getId()), end="\n")
            print("Cliente: " + i.getNome(), end="\n")
            print("Idade: " + str(i.getIdade()), end="\n")
            print("Email: " + i.getEmail(), end="\n")
            print("---------------------------------")

    print("Não existe nenhum registro")
    continuar = input("Pressione enter para continuar...")

    while(continuar != ''):
        time.sleep(1)

    clear()

############# DELETANDO O CLIENTE ##############
def deletar_cliente():
    id_cliente = int(input("Digite o ID do cliente que deseja deletar: "))

    for cliente in lista_cliente:
        if(cliente.getId() == id_cliente):
            lista_cliente.remove(cliente)

    print("Cliente deletado com sucesso")
    time.sleep(1)
    clear()
    salvar_alteracoes()

############# EDITANDO O CLIENTE ##############
def editar_cliente():
    id_cliente = int(input("Digite o ID do cliente que deseja editar: "))

    for cliente in lista_cliente:
        if cliente.getId() == id_cliente:
            if input("Deseja editar o nome? S/N ").upper() == "S": nome = input("\nDigite o nome do cliente: (" + cliente.getNome() + ") ")
            else: nome = cliente.getNome()

            if input("Deseja editar a idade? S/N ").upper() == "S": idade = input("Digite a idade do cliente: (" + cliente.getIdade() + ") ")
            else: idade = cliente.getIdade()

            if input("Deseja editar o email? S/N ").upper() == "S": email = input("Digite o email do cliente: (" + cliente.getEmail() + ") ")
            else: email = cliente.getEmail()

            if cliente.setNome(nome) and cliente.setIdade(idade) and cliente.setEmail(email):
                print("Cliente editado com sucesso")
            else:
                print("O cliente nao foi editado")

    time.sleep(1)    
    clear()
    salvar_alteracoes()

############# SALVANDO AS ALTERACOES ##############
def salvar_alteracoes():
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
#if re.match("([a-z]|[a-z]\d)@[a-z]",input()) != None:
#    print("Okay")
#else:
#    print("Not okay")

while(opcao != 0):
    print("Bem vindo ao cadastro de clientes\nSelecione uma opçao abaixo:\n")
    print("[1] - Cadastrar cliente")
    print("[2] - Visualizar clientes cadastrados")
    print("[3] - Deletar cliente")
    print("[4] - Editar cliente")
    print("[0] - Sair")

    try:
        opcao = int(sys.stdin.readline())

        clear()

        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            visualizar_clientes()
        elif opcao == 3:
            deletar_cliente()
        elif opcao == 4:
            editar_cliente()
        elif opcao == 0:
            salvar_alteracoes()
        else:
            print("Opção invalida")
    except ValueError:
        clear()
        print("Opção invalida")

