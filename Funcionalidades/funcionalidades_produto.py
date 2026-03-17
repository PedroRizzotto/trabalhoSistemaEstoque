import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Models.Produto import Produto
from Models.Salvamento import salvar_produtos


def proximo_id_produto(lista_produtos):
    # pega o maior id e retorna +1
    if lista_produtos.is_empty():
        return 1

    maior_id = 0
    atual = lista_produtos.head

    while atual is not None:
        if atual.valor.id_produto > maior_id:
            maior_id = atual.valor.id_produto
        atual = atual.proximo

    return maior_id + 1


def cadastrar_produto(lista_produtos, pilha_operacoes):
    try:
        nome = input("Digite o nome do produto: ").strip()
        if not nome:
            print("Erro: o nome do produto nao pode ser vazio.")
            return

        # ve se ja existe produto com esse nome
        atual = lista_produtos.head
        while atual is not None:
            if atual.valor.nome.lower() == nome.lower():
                print(f"Erro: ja existe um produto com o nome '{nome}'.")
                return
            atual = atual.proximo

        quantidade_str = input("Digite a quantidade em estoque: ").strip()
        try:
            quantidade = int(quantidade_str)
        except ValueError:
            print("Erro: a quantidade deve ser um numero inteiro.")
            return

        if quantidade < 0:
            print("Erro: a quantidade nao pode ser negativa.")
            return

        preco_str = input("Digite o preco do produto: ").strip()
        try:
            preco = float(preco_str)
        except ValueError:
            print("Erro: o preco deve ser um numero valido.")
            return

        if preco <= 0:
            print("Erro: o preco deve ser maior que zero.")
            return

        id_produto = proximo_id_produto(lista_produtos)
        novo_produto = Produto(id_produto, nome, quantidade, preco)
        lista_produtos.inserir_fim(novo_produto)

        salvar_produtos(lista_produtos)

        # coloca na pilha pra desfazer
        pilha_operacoes.push({
            "tipo": "cadastro_produto",
            "dados": novo_produto
        })

        print(f"Produto '{nome}' cadastrado com sucesso! (ID: {id_produto})")

    except Exception as e:
        print(f"Erro ao cadastrar produto: {e}")


def listar_produtos(lista_produtos):
    if lista_produtos.is_empty():
        print("Nenhum produto cadastrado.")
        return

    print("\n===== PRODUTOS EM ESTOQUE =====")
    print(f"{'ID':<6} {'Nome':<25} {'Qtd':>6} {'Preco':>12}")
    print("-" * 49)

    atual = lista_produtos.head
    while atual is not None:
        p = atual.valor
        print(f"{p.id_produto:<6} {p.nome:<25} {p.quantidade:>6} R$ {p.preco:>8.2f}")
        atual = atual.proximo

    print(f"\nTotal: {lista_produtos.quantidade_itens}")


def pesquisar_produto(lista_produtos):
    if lista_produtos.is_empty():
        print("Nenhum produto cadastrado.")
        return

    termo = input("Digite o ID ou nome do produto: ").strip()
    if not termo:
        print("Erro: digite algo pra pesquisar.")
        return

    encontrados = []
    atual = lista_produtos.head

    while atual is not None:
        p = atual.valor

        # tenta ver se digitou um id
        try:
            if p.id_produto == int(termo):
                encontrados.append(p)
        except ValueError:
            pass

        # busca por nome tambem
        if termo.lower() in p.nome.lower():
            if p not in encontrados:
                encontrados.append(p)

        atual = atual.proximo

    if not encontrados:
        print(f"Nenhum produto encontrado pra '{termo}'.")
        return

    print(f"\n===== RESULTADO DA PESQUISA =====")
    print(f"{'ID':<6} {'Nome':<25} {'Qtd':>6} {'Preco':>12}")
    print("-" * 49)

    for p in encontrados:
        print(f"{p.id_produto:<6} {p.nome:<25} {p.quantidade:>6} R$ {p.preco:>8.2f}")

    print(f"\n{len(encontrados)} produto(s) encontrado(s).")


def exibir_valor_total_estoque(lista_produtos):
    if lista_produtos.is_empty():
        print("Nenhum produto cadastrado.")
        return

    total = 0.0
    atual = lista_produtos.head

    while atual is not None:
        p = atual.valor
        total += p.quantidade * p.preco
        atual = atual.proximo

    print(f"\nValor total do estoque: R$ {total:.2f}")


def buscar_produto_por_id(lista_produtos, id_produto):
    # percorre a lista ate achar o produto com esse id
    atual = lista_produtos.head
    while atual is not None:
        if atual.valor.id_produto == id_produto:
            return atual.valor
        atual = atual.proximo
    return None
