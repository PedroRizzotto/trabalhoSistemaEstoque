class Fila:

    def __init__(self):
        self._itens = []

    def enfileirar(self, item):
        self._itens.append(item) # sempre vai adicionar no final da lista

    def desinfileirar(self):
        if self.is_empty(): # a verdade para desinfileirar, é que precisar ter algum dado na fila
            print("A fila está vazia")
            return
        
        self._itens.pop(0)

    def proximo_a_sair_da_fila(self):
        print(self._itens[0])
    
    def is_empty(self):
        return len(self._itens) == 0
    
    def __len__(self):
        return len(self._itens)

    def __str__(self): # representacao da fila como uma lista
        return str(self._itens)
