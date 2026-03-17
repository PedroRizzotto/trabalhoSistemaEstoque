import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.Venda import Venda
from Models.Salvamento import salvar_vendas, salvar_produtos, salvar_clientes
from Funcionalidades.funcionalidades_clientes import buscar_cliente_por_id
from Funcionalidades.funcionalidades_produto import buscar_produto_por_id


def proximo_id_venda(fila_vendas):
    if fila_vendas.is_empty():
        return 1

    maior_id = 0
    for venda in fila_vendas._itens:
        if venda.id_venda > maior_id:
            maior_id = venda.id_venda

    return maior_id + 1


def realizar_venda(lista_clientes, lista_produtos, fila_vendas, pilha_operacoes):
    try:
        # pede o cliente
        id_cliente_str = input("Digite o ID do cliente: ").strip()
        try:
            id_cliente = int(id_cliente_str)
        except ValueError:
            print("Erro: o ID do cliente deve ser um numero.")
            return

        cliente = buscar_cliente_por_id(lista_clientes, id_cliente)
        if cliente is None:
            print(f"Erro: cliente com ID {id_cliente} nao encontrado.")
            return

        # pede o produto
        id_produto_str = input("Digite o ID do produto: ").strip()
        try:
            id_produto = int(id_produto_str)
        except ValueError:
            print("Erro: o ID do produto deve ser um numero.")
            return

        produto = buscar_produto_por_id(lista_produtos, id_produto)
        if produto is None:
            print(f"Erro: produto com ID {id_produto} nao encontrado.")
            return

        # pede a quantidade
        quantidade_str = input("Digite a quantidade: ").strip()
        try:
            quantidade = int(quantidade_str)
        except ValueError:
            print("Erro: a quantidade deve ser um numero inteiro.")
            return

        if quantidade <= 0:
            print("Erro: a quantidade tem que ser maior que zero.")
            return

        if quantidade > produto.quantidade:
            print(f"Erro: estoque insuficiente. Disponivel: {produto.quantidade}")
            return

        # cria a venda
        valor_total = quantidade * produto.preco
        id_venda = proximo_id_venda(fila_vendas)
        nova_venda = Venda(id_venda, cliente, produto, quantidade, valor_total)

        # atualiza o estoque
        produto.quantidade -= quantidade

        # coloca na fila
        fila_vendas.enfileirar(nova_venda)

        # salva nos csvs
        salvar_vendas(fila_vendas)
        salvar_produtos(lista_produtos)

        # coloca na pilha pra desfazer
        pilha_operacoes.push({
            "tipo": "venda",
            "dados": nova_venda
        })

        print(f"Venda realizada com sucesso!")
        print(f"  Cliente: {cliente.nome}")
        print(f"  Produto: {produto.nome}")
        print(f"  Quantidade: {quantidade}")
        print(f"  Valor total: R$ {valor_total:.2f}")

    except Exception as e:
        print(f"Erro ao realizar venda: {e}")


def ver_fila_vendas(fila_vendas):
    if fila_vendas.is_empty():
        print("Nenhuma venda registrada.")
        return

    print("\n===== FILA DE VENDAS =====")
    print(f"{'ID':<6} {'Cliente':<20} {'Produto':<20} {'Qtd':>5} {'Total':>12}")
    print("-" * 63)

    for venda in fila_vendas._itens:
        print(
            f"{venda.id_venda:<6} "
            f"{venda.cliente.nome:<20} "
            f"{venda.produto.nome:<20} "
            f"{venda.quantidade:>5} "
            f"R$ {venda.valor_total:>8.2f}"
        )

    print(f"\nTotal de vendas: {len(fila_vendas)}")


def exibir_valor_total_vendas(fila_vendas):
    if fila_vendas.is_empty():
        print("Nenhuma venda registrada.")
        return

    total = 0.0
    for venda in fila_vendas._itens:
        total += venda.valor_total

    print(f"\nValor total de vendas: R$ {total:.2f}")


def desfazer_operacao(lista_clientes, lista_produtos, fila_vendas, pilha_operacoes):
    if pilha_operacoes.is_empty():
        print("Nenhuma operacao pra desfazer.")
        return

    try:
        operacao = pilha_operacoes.pop()
        tipo = operacao["tipo"]
        dados = operacao["dados"]

        if tipo == "cadastro_cliente":
            remover_cliente(lista_clientes, dados.id_cliente)
            salvar_clientes(lista_clientes)
            print(f"Cadastro do cliente '{dados.nome}' desfeito.")

        elif tipo == "cadastro_produto":
            remover_produto(lista_produtos, dados.id_produto)
            salvar_produtos(lista_produtos)
            print(f"Cadastro do produto '{dados.nome}' desfeito.")

        elif tipo == "venda":
            # devolve pro estoque
            produto = buscar_produto_por_id(lista_produtos, dados.produto.id_produto)
            if produto is not None:
                produto.quantidade += dados.quantidade

            # tira da fila
            remover_venda(fila_vendas, dados.id_venda)

            salvar_produtos(lista_produtos)
            salvar_vendas(fila_vendas)
            print(f"Venda #{dados.id_venda} desfeita. Estoque restaurado.")

        else:
            print("Tipo de operacao desconhecido.")

    except Exception as e:
        print(f"Erro ao desfazer operacao: {e}")


# funcoes auxiliares pra remover das estruturas

def remover_cliente(lista_clientes, id_cliente):
    if lista_clientes.is_empty():
        return

    # se for o primeiro
    if lista_clientes.head.valor.id_cliente == id_cliente:
        lista_clientes.remover_inicio()
        return

    anterior = lista_clientes.head
    atual = anterior.proximo

    while atual is not None:
        if atual.valor.id_cliente == id_cliente:
            anterior.proximo = atual.proximo
            if atual == lista_clientes.tail:
                lista_clientes.tail = anterior
            lista_clientes.quantidade_itens -= 1
            return
        anterior = atual
        atual = atual.proximo


def remover_produto(lista_produtos, id_produto):
    if lista_produtos.is_empty():
        return

    if lista_produtos.head.valor.id_produto == id_produto:
        lista_produtos.remover_inicio()
        return

    anterior = lista_produtos.head
    atual = anterior.proximo

    while atual is not None:
        if atual.valor.id_produto == id_produto:
            anterior.proximo = atual.proximo
            if atual == lista_produtos.tail:
                lista_produtos.tail = anterior
            lista_produtos.quantidade_itens -= 1
            return
        anterior = atual
        atual = atual.proximo


def remover_venda(fila_vendas, id_venda):
    for i in range(len(fila_vendas._itens)):
        if fila_vendas._itens[i].id_venda == id_venda:
            fila_vendas._itens.pop(i)
            return
