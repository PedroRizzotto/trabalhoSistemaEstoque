import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.Cliente import Cliente
from Models.Salvamento import salvar_clientes


def proximo_id_cliente(lista_clientes):
    # pega o maior id que existe e retorna +1
    if lista_clientes.is_empty():
        return 1

    maior_id = 0
    atual = lista_clientes.head

    while atual is not None:
        if atual.valor.id_cliente > maior_id:
            maior_id = atual.valor.id_cliente
        atual = atual.proximo

    return maior_id + 1


def cadastrar_cliente(lista_clientes, pilha_operacoes):
    try:
        nome = input("Digite o nome do cliente: ").strip()

        if not nome:
            print("Erro: o nome nao pode ser vazio.")
            return

        # ve se ja tem cliente com esse nome
        atual = lista_clientes.head
        while atual is not None:
            if atual.valor.nome.lower() == nome.lower():
                print(f"Erro: ja existe um cliente com o nome '{nome}'.")
                return
            atual = atual.proximo

        id_cliente = proximo_id_cliente(lista_clientes)
        novo_cliente = Cliente(id_cliente, nome)
        lista_clientes.inserir_fim(novo_cliente)

        salvar_clientes(lista_clientes)

        # coloca na pilha pra poder desfazer depois
        pilha_operacoes.push({
            "tipo": "cadastro_cliente",
            "dados": novo_cliente
        })

        print(f"Cliente '{nome}' cadastrado com sucesso! (ID: {id_cliente})")

    except Exception as e:
        print(f"Erro ao cadastrar cliente: {e}")


def listar_clientes(lista_clientes):
    if lista_clientes.is_empty():
        print("Nenhum cliente cadastrado.")
        return

    print("\n===== CLIENTES CADASTRADOS =====")
    print(f"{'ID':<6} {'Nome':<30}")
    print("-" * 36)

    atual = lista_clientes.head
    while atual is not None:
        c = atual.valor
        print(f"{c.id_cliente:<6} {c.nome:<30}")
        atual = atual.proximo

    print(f"\nTotal: {lista_clientes.quantidade_itens}")


def exibir_clientes_gastos(lista_clientes, fila_vendas):
    if lista_clientes.is_empty():
        print("Nenhum cliente cadastrado.")
        return

    print("\n===== CLIENTES E VALORES GASTOS =====")
    print(f"{'ID':<6} {'Nome':<25} {'Total Gasto':>15}")
    print("-" * 46)

    atual = lista_clientes.head

    while atual is not None:
        cliente = atual.valor
        total = 0.0

        # percorre todas as vendas pra somar o que esse cliente gastou
        for i in range(len(fila_vendas)):
            venda = fila_vendas._itens[i]
            if venda.cliente.id_cliente == cliente.id_cliente:
                total += venda.valor_total

        print(f"{cliente.id_cliente:<6} {cliente.nome:<25} R$ {total:>10.2f}")
        atual = atual.proximo

    print()


def buscar_cliente_por_id(lista_clientes, id_cliente):
    # percorre a lista ate achar o cliente com esse id
    atual = lista_clientes.head
    while atual is not None:
        if atual.valor.id_cliente == id_cliente:
            return atual.valor
        atual = atual.proximo
    return None
