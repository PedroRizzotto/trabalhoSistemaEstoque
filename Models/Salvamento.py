import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.Cliente import Cliente
from Models.Produto import Produto
from Models.Venda import Venda


PASTA_DADOS = os.path.join(os.path.dirname(__file__), '..')
ARQUIVO_CLIENTES = os.path.join(PASTA_DADOS, 'clientes.csv')
ARQUIVO_PRODUTOS = os.path.join(PASTA_DADOS, 'produtos.csv')
ARQUIVO_VENDAS = os.path.join(PASTA_DADOS, 'vendas.csv')




def salvar_clientes(lista_clientes):
    try:
        with open(ARQUIVO_CLIENTES, 'w', encoding='utf-8') as arquivo:
            arquivo.write("id_cliente;nome\n")

            atual = lista_clientes.head
            while atual is not None:
                c = atual.valor
                arquivo.write(f"{c.id_cliente};{c.nome}\n")
                atual = atual.proximo
    except Exception as e:
        print(f"Erro ao salvar clientes: {e}")


def carregar_clientes(lista_clientes):
    if not os.path.exists(ARQUIVO_CLIENTES):
        return

    try:
        with open(ARQUIVO_CLIENTES, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        for i in range(1, len(linhas)):  
            linha = linhas[i].strip()
            if not linha:
                continue

            partes = linha.split(';')
            if len(partes) < 2:
                continue

            try:
                id_cliente = int(partes[0])
                nome = partes[1]

                if nome:
                    cliente = Cliente(id_cliente, nome)
                    lista_clientes.inserir_fim(cliente)
            except ValueError:
                
                continue

    except Exception as e:
        print(f"Erro ao carregar clientes: {e}")




def salvar_produtos(lista_produtos):
    try:
        with open(ARQUIVO_PRODUTOS, 'w', encoding='utf-8') as arquivo:
            arquivo.write("id_produto;nome;quantidade;preco\n")

            atual = lista_produtos.head
            while atual is not None:
                p = atual.valor
                arquivo.write(f"{p.id_produto};{p.nome};{p.quantidade};{p.preco}\n")
                atual = atual.proximo
    except Exception as e:
        print(f"Erro ao salvar produtos: {e}")


def carregar_produtos(lista_produtos):
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return

    try:
        with open(ARQUIVO_PRODUTOS, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        for i in range(1, len(linhas)):
            linha = linhas[i].strip()
            if not linha:
                continue

            partes = linha.split(';')
            if len(partes) < 4:
                continue

            try:
                id_produto = int(partes[0])
                nome = partes[1]
                quantidade = int(partes[2])
                preco = float(partes[3])

                if nome:
                    produto = Produto(id_produto, nome, quantidade, preco)
                    lista_produtos.inserir_fim(produto)
            except ValueError:
                continue

    except Exception as e:
        print(f"Erro ao carregar produtos: {e}")



def salvar_vendas(fila_vendas):
    try:
        with open(ARQUIVO_VENDAS, 'w', encoding='utf-8') as arquivo:
            arquivo.write("id_venda;id_cliente;nome_cliente;id_produto;nome_produto;quantidade;valor_total\n")

            for venda in fila_vendas._itens:
                arquivo.write(
                    f"{venda.id_venda};"
                    f"{venda.cliente.id_cliente};"
                    f"{venda.cliente.nome};"
                    f"{venda.produto.id_produto};"
                    f"{venda.produto.nome};"
                    f"{venda.quantidade};"
                    f"{venda.valor_total}\n"
                )
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")


def carregar_vendas(fila_vendas, lista_clientes, lista_produtos):
   
    if not os.path.exists(ARQUIVO_VENDAS):
        return

    try:
        with open(ARQUIVO_VENDAS, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        for i in range(1, len(linhas)):
            linha = linhas[i].strip()
            if not linha:
                continue

            partes = linha.split(';')
            if len(partes) < 7:
                continue

            try:
                id_venda = int(partes[0])
                id_cliente = int(partes[1])
                id_produto = int(partes[3])
                quantidade = int(partes[5])
                valor_total = float(partes[6])

                cliente = buscar_na_lista_por_id(lista_clientes, id_cliente, "cliente")
                produto = buscar_na_lista_por_id(lista_produtos, id_produto, "produto")

                if cliente is None or produto is None:
                    continue

                venda = Venda(id_venda, cliente, produto, quantidade, valor_total)
                fila_vendas.enfileirar(venda)

            except ValueError:
                continue

    except Exception as e:
        print(f"Erro ao carregar vendas: {e}")


def buscar_na_lista_por_id(lista, id_buscado, tipo):
    atual = lista.head
    while atual is not None:
        if tipo == "cliente" and atual.valor.id_cliente == id_buscado:
            return atual.valor
        elif tipo == "produto" and atual.valor.id_produto == id_buscado:
            return atual.valor
        atual = atual.proximo
    return None
