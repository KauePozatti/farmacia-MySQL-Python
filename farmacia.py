import os 
os.system("CLS")
import mysql.connector

conexao = mysql.connector.connect(
        host="localhost",
        user="Projetos",
        password="223816",
        database="farmacia"
    )
if conexao.is_connected():
        print("Conexão realizada com sucesso!")
        cursor = conexao.cursor() 

def cadastrar_clientes(cursor, conexao):
        print("Seja Bem Vindo a Farmacia!, nos forneça algumas informações para realizarmos seu cadastro!: ")

        nome = str(input("Digite seu nome completo: ")).lower()
        telefone = input("Digite seu telefone: ").strip()
        email = str(input("Digite seu melhor e-mail: "))
        endereco = str(input("Digite seu endereço: ")).lower()

        comando = '''
        insert into clientes (nome, telefone, email, endereco) 
        values (%s, %s, %s, %s)
        '''

        valores = (nome, telefone, email, endereco)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n Cliente cadastrado com sucesso!")

def cadastrar_produto(cursor, conexao):
        print("Cadastro de produtos...")

        nome = str(input("Nome do produto: ")).lower()
        descricao = str(input("Descrição do produto: ")).lower()
        preco = float(input("Valor do produto: "))
        quantidade_estoque = int(input("Quantidade em estoque: "))
        data_validade = input("Data de validade (AAAA-MM-DD): ").strip()

        comando = '''
        insert into produtos (nome, descricao, preco, quantidade_estoque, data_validade)
        values (%s, %s, %s, %s, %s)
        '''

        valores = (nome, descricao, preco, quantidade_estoque, data_validade)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n Produto cadastrado com sucesso!")

def registro_venda(cursor, conexao):
        print("Registro da venda")

        cliente_id = int(input("Digite o ID do cliente: "))
        data_venda = input("Data de validade (AAAA-MM-DD): ").strip()
        total = float(input("Digite o total: "))

        comando = '''
        insert into vendas (cliente_id, data_venda, total)
        values (%s, %s, %s)
        '''

        valores = (cliente_id, data_venda, total)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n Registro realizado com sucesso!")

def itens_venda(cursor, conexao): 
        print("Itens da venda")

        quantidade = int(input("Quantidade vendida: "))
        preco_unitario = float(input("Preço unitario: "))
        subtotal = float(input("Subtotal: ").strip())
        venda_id = int(input("Digite o ID da venda: ").strip())
        produto_id = int(input("Digite o ID do produto: ")).strip()

        comando = '''
        insert into itens_venda (quantidade, preco_unitario, subtotal, venda_id, produto_id)
        values (%s, %s, %s, %s, %s)
        '''

        valores = (quantidade, preco_unitario, subtotal, venda_id, produto_id)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n Itens da venda cadastrado com sucesso!")

def cadastrar_fornecedores(cursor, conexao):
        print("Cadastro de fornecedores")

        nome = str(input("Digite seu nome completo: ")).lower()
        cnpj = input("Digite o cnpj: ").strip()
        telefone = input("Digite seu telefone: ").strip()
        email = str(input("Digite seu melhor e-mail: "))

        comando = '''
        insert into fornecedores (nome, cnpj, telefone, email)
        values (%s, %s, %s, %s)
        '''

        valores = (nome, cnpj, telefone, email)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n Fornecedor cadastrado com sucesso!")

def compras(cursor, conexao):
        print("Compras")

        data_compra = input("Data de validade (AAAA-MM-DD): ").strip()
        total = float(input("Digite o total: ").strip())
        fornecedor_id = int(input("Digite o ID do fornecedor: ").strip())

        comando = '''
        insert into compras (data_compra, total, fornecedor_id)
        values (%s, %s, %s)
        '''

        valores = (data_compra, total, fornecedor_id)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n compras com sucesso!")

def itens_compra(cursor, conexao):
        print("Itens da compra")

        quantidade = int(input("Quantidade vendida: "))
        preco_unitario = float(input("Preço unitario: "))
        subtotal = float(input("Subtotal: ").strip())
        compra_id = int(input("Digite o ID da compra: ").strip())
        produto_id = int(input("Digite o ID do produto: ").strip())

        comando = '''
        insert into itens_compra (quantidade, preco_unitario, subtotal, compra_id, produto_id)
        values (%s, %s, %s, %s, %s)
        '''

        valores = (quantidade, preco_unitario, subtotal, compra_id, produto_id)
        cursor.execute(comando, valores)
        conexao.commit()
        print("\n Itens da compra cadastrado com sucesso!")

while True:
    print("\n==== MENU FARMÁCIA ====")
    print("1 - Cadastrar Cliente")
    print("2 - Cadastrar Produto")
    print("3 - Registrar Venda")
    print("4 - Registrar Itens da Venda")
    print("5 - Cadastrar Fornecedor")
    print("6 - Registrar Compra")
    print("7 - Registrar Itens da Compra")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_clientes(cursor, conexao)
    elif opcao == "2":
        cadastrar_produto(cursor, conexao)
    elif opcao == "3":
        registro_venda(cursor, conexao)
    elif opcao == "4":
        itens_venda(cursor, conexao)
    elif opcao == "5":
        cadastrar_fornecedores(cursor, conexao)
    elif opcao == "6":
        compras(cursor, conexao)
    elif opcao == "7":
        itens_compra(cursor, conexao)
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

conexao.close()
cursor.close()
print("Conexão encerrada com sucesso!")