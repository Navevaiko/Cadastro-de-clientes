import sys
import os
import ClienteClass

lista_cliente = []


def cadastrar_cliente():
    cliente = ClienteClass.Cliente()

    nome = input("\nDigite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    email = input("Digite o email do cliente: ")

    if(cliente.setNome(nome) and cliente.setIdade(idade) and cliente.setEmail(email)):
        lista_cliente.append(cliente)
        print("Cliente cadastrado com sucesso")
    else:
        print("O cliente nao foi cadastro")

    print("\n")

def visualizar_clientes():
    print("\n" * 5)
    for i in lista_cliente:
        print("Cliente: " + i.getNome())

def deletar_cliente():
    for i in lista_cliente:
        print("Nada")

def rotina_saida():
    clientes_cadastados = open("clientes_cadastrados.txt", "+a")

    for cliente in lista_cliente:
        clientes_cadastados.write(cliente.getNome() + "," + cliente.getIdade() + "," + cliente.getEmail() + "\n")

    clientes_cadastados.close()

def inicializar():
    if(os.path.isfile("clientes_cadastrados.txt")):
        clientes_cadastados = open("clientes_cadastrados.txt", "r")

        if(clientes_cadastados.readlines()):
            for linha in clientes_cadastados:

                linha_array = linha.split(",")

                cliente = ClienteClass.Cliente()

                cliente.setNome(linha_array[0])
                cliente.setIdade(linha_array[1])
                cliente.setEmail(linha_array[2])
                lista_cliente.append(cliente)

############# MAIN ##############
opcao = 1

inicializar()

############# MENU ##############
while(opcao != 0):
    print("Bem vindo ao cadastro de clientes\nSelecione uma opçao abaixo:\n")
    print("[1] - Cadastrar cliente")
    print("[2] - Visualizar clientes cadastrados")
    print("[3] - Deletar cliente")
    print("[0] - Sair")

    opcao = int(sys.stdin.readline())

    if opcao == 1:
        cadastrar_cliente()
    elif opcao == 2:
        visualizar_clientes()
    elif opcao == 0:
        rotina_saida()


