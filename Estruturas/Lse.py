from Nodo import Nodo

class LSE:

    def __init__(self):
        self.head = None
        self.tail = None
        self.quantidade_itens = 0

    def is_empty(self):
        return self.quantidade_itens == 0 or self.head == None

    def inserir_inicio(self, dado_a_ser_inserido):
        self.quantidade_itens += 1

        if self.is_empty():
            # se a lista estiver vazia, o inicio e o fim serão o mesmo dado
            nodo = Nodo(dado_a_ser_inserido)
            self.head = nodo # ocupa o mesmo nodo do tail
            self.tail = nodo # ocupa o mesmo nodo do head
            return
        
        # lista ja possui itens
        head_armazenado = self.head # variavel para armazenar o head atual
        self.head = Nodo(dado_a_ser_inserido) # atualizmos o head para o novo valor
        self.head.proximo = head_armazenado # linkamos o novo head com o restante da lista através do .proximo

    def inserir_fim(self, dado_a_ser_inserido):
        self.quantidade_itens += 1

        if self.is_empty():
            # se a lista estiver vazia, o inicio e o fim serão o mesmo dado
            nodo = Nodo(dado_a_ser_inserido)
            self.head = nodo # ocupa o mesmo nodo do tail
            self.tail = nodo # ocupa o mesmo nodo do head
            return

        # lista ja possui itens
        tail_armazenado = self.tail
        nodo = Nodo(dado_a_ser_inserido) # cria um nodo
        tail_armazenado.proximo = nodo
        self.tail = nodo

    def remover_inicio(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        self.quantidade_itens -= 1

        if self.head == self.tail: # se for um único dado na lista
            dado_removido = self.tail
            self.head = None
            self.tail = None
            return dado_removido
        
        # se possuir mais de um
        dado_removido = self.head
        self.head = dado_removido.proximo
        dado_removido.proximo = None

        return dado_removido
        
    def remover_fim(self):
        if self.is_empty():
            print("A lista está vazia.")
            return
        
        self.quantidade_itens -= 1

        if self.head == self.tail: # se for um único dado na lista
            dado_removido = self.tail
            self.head = None
            self.tail = None
            return dado_removido
        
        # se possuir mais do que um item na lista
        dado_removido = None
        atual = self.head

        while atual != None:
            if (atual.proximo != None and atual.proximo == self.tail):
                dado_removido = self.tail
                self.tail = atual # o atual é o penultimo item da lista
                atual.proximo = None
                return dado_removido
            
            atual = atual.proximo

    def imprimir_lista_completa(self):
        atual = self.head
        while atual != None:
            print(atual)
            atual = atual.proximo

    def imprimir_lado_a_lado(self):
        saida = ""
        atual = self.head

        while atual != None:
            if atual == self.head:
                saida += '[' + str(atual) + ']'
            else:
                saida += '=>' + '[' + str(atual) + ']'

            atual = atual.proximo
            
        print(saida)