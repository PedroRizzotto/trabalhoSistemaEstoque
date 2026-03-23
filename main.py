import sys
import os
sys.path.append(os.path.dirname(__file__))

import time
from Estruturas.Lse import LSE
from Estruturas.Fila import Fila
from Estruturas.Pilha import Pilha
from Models.Salvamento import *
from Funcionalidades.funcionalidades_clientes import *
from Funcionalidades.funcionalidades_produto import *
from Funcionalidades.funcionalidades_venda import *

def exibir_menu():
    print("\n===== MENU ESTOQUE =====")
    print("1  - Cadastrar cliente")
    print("2  - Listar clientes")
    print("3  - Cadastrar produto")
    print("4  - Listar produtos")
    print("5  - Pesquisar produto")
    print("6  - Realizar venda")
    print("7  - Ver fila de vendas")
    print("8  - Desfazer ultima operacao")
    print("9  - Exibir valor total do estoque")
    print("10 - Exibir valor total de vendas")
    print("11 - Exibir clientes e valores gastos")
    print("12 - Sair")
    print("========================")


def main():
    lista_clientes = LSE()
    lista_produtos = LSE()
    fila_vendas = Fila()
    pilha_operacoes = Pilha()

    carregar_clientes(lista_clientes)
    carregar_produtos(lista_produtos)
    carregar_vendas(fila_vendas, lista_clientes, lista_produtos)

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente(lista_clientes, pilha_operacoes)

        elif opcao == "2":
            listar_clientes(lista_clientes)

        elif opcao == "3":
            cadastrar_produto(lista_produtos, pilha_operacoes)

        elif opcao == "4":
            listar_produtos(lista_produtos)

        elif opcao == "5":
            pesquisar_produto(lista_produtos)

        elif opcao == "6":
            realizar_venda(lista_clientes, lista_produtos, fila_vendas, pilha_operacoes)

        elif opcao == "7":
            ver_fila_vendas(fila_vendas)

        elif opcao == "8":
            desfazer_operacao(lista_clientes, lista_produtos, fila_vendas, pilha_operacoes)

        elif opcao == "9":
            exibir_valor_total_estoque(lista_produtos)

        elif opcao == "10":
            exibir_valor_total_vendas(fila_vendas)

        elif opcao == "11":
            exibir_clientes_gastos(lista_clientes, fila_vendas)

        elif opcao == "12":
            break

        else:
            print("Opção inválida! Digite um número de 1 a 12")

        time.sleep(2)


if __name__ == "__main__":
    main()