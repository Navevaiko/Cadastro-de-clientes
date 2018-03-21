import sys
import os
import time
import re
import ClienteClass

lista_cliente = []
nome_arquivo = "clientes_cadastrados.txt"

############# PESQUISANDO O CLIENTE ##############
def pesquisar_cliente():
    cpf_cliente = input("Digite o CPF do cliente que deseja pesquisar: ")
    encontrou = 0
    
    print("\n" * 5)
    if len(lista_cliente):
        for i in lista_cliente:
            if i.getCpf() == cpf_cliente:
                encontrou = 1
                
                print("ID: " + str(i.getId()), end="\n")
                print("Cliente: " + i.getNome(), end="\n")
                print("Idade: " + str(i.getIdade()), end="\n")
                print("Email: " + i.getEmail(), end="\n")
                print("CPF: " + i.getCpf(), end="\n")
                print("---------------------------------")

    if not encontrou: print("Nenhum registro encontrado")
    
    continuar = input("Pressione enter para continuar...")

    while(continuar != ''):
        time.sleep(1)

    clear()

############# LIMPA O CONSOLE ##############
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
    cpf   = input("Digite o CPF do cliente: ")
   
    try:
        if cliente.setId(id) and cliente.setNome(nome) and cliente.setIdade(int(idade)) and cliente.setEmail(email) and cliente.setCpf(cpf):
            lista_cliente.append(cliente)
            print("Cliente cadastrado com sucesso")
        else:
            print("O cliente nao foi cadastrado")
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
            print("CPF: " + i.getCpf(), end="\n")
            print("---------------------------------")

    else: print("Não existe nenhum registro")
    
    continuar = input("Pressione enter para continuar...")
    while(continuar != ''):
        time.sleep(1)

    clear()

############# DELETANDO O CLIENTE ##############
def deletar_cliente():
    cpf_cliente = input("Digite o CPF do cliente que deseja deletar: ")
    encontrou = 0
    
    for cliente in lista_cliente:
        if(cliente.getCpf() == cpf_cliente):
            lista_cliente.remove(cliente)

    if encontrou: print("Cliente deletado com sucesso")
    else: print("Nenhum registro encontrado")
    
    time.sleep(1)
    clear()
    salvar_alteracoes()

############# EDITANDO O CLIENTE ##############
def editar_cliente():
    cpf_cliente = input("Digite o CPF do cliente que deseja editar: ")

    encontrou = 0
    
    for cliente in lista_cliente:
        if cliente.getCpf() == cpf_cliente:
            encontrou = 1
            
            if input("Deseja editar o nome? S/N ").upper() == "S": nome = input("\nDigite o nome do cliente: (" + cliente.getNome() + ") ")
            else: nome = cliente.getNome()

            if input("Deseja editar a idade? S/N ").upper() == "S": idade = input("Digite a idade do cliente: (" + cliente.getIdade() + ") ")
            else: idade = cliente.getIdade()

            if input("Deseja editar o email? S/N ").upper() == "S": email = input("Digite o email do cliente: (" + cliente.getEmail() + ") ")
            else: email = cliente.getEmail()

            if input("Deseja editar o CPF? S/N ").upper() == "S": cpf = input("Digite o CPF do cliente: (" + cliente.getCpf() + ") ")
            else: cpf = cliente.getCpf()

            if cliente.setNome(nome) and cliente.setIdade(idade) and cliente.setEmail(email) and cliente.setCpf(cpf):
                print("Cliente editado com sucesso")
            else:
                print("O cliente nao foi editado")

    if not encontrou: print("Nenhum registro encontrado")
    time.sleep(1)    
    clear()
    salvar_alteracoes()

############# SALVANDO AS ALTERACOES ##############
def salvar_alteracoes():
    clientes_cadastados = open(nome_arquivo, "w+")

    for cliente in lista_cliente:
        clientes_cadastados.write(str(cliente.getId()) + "," + cliente.getNome() + "," + str(cliente.getIdade()) + "," + cliente.getEmail() + "," + cliente.getCpf() + "\n")

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
            cliente.setIdade(int(linha_array[2]))
            cliente.setEmail(linha_array[3])
            cliente.setCpf(linha_array[4])
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
    print("[5] - Pesquisar cliente")
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
        elif opcao == 5:
            pesquisar_cliente()
        elif opcao == 0:
            salvar_alteracoes()
        else:
            print("Opção invalida")
    except ValueError:
        clear()
        print("Opção invalida")

