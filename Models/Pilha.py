class Pilha:

    def __init__(self):
        self._itens = [] # a lista de itens sempre começa vazia, só pode ser adicionado dados pelo metodo push

    def push(self, item): # adiciona o item sempre no topo da pilha
        self._itens.append(item) # na pilha, o topo é sempre o ultimo dado da lista (ou seja, o final da lista)

    def pop(self): # sempre remove o item do topo da pilha
        if self.is_empty():
            raise IndexError("Não é possível remover dados da pilha, pois a pilha está vazia")

        return self._itens.pop() # retorna o topo, porém remove da pilha

    def peek(self): # sempre retorna o item do topo da pilha
        if self.is_empty():
            raise IndexError("Não é possível retornar o topo da pilha, pois a pilha está vazia")

        return self._itens[-1] # retorna o topo, porém não remove da pilha

    def is_empty(self): # verifica se a nossa ta vazia
        return len(self._itens) == 0 # verifica se a quantidade de dados dentro da lista é igual a zero

    def __str__(self): # retorna o valor formatado da pilha
        return str(self._itens) # retorna a lista. ex: ["A", "B", "C"]
    
    def __len__(self): # retorna a quantidade de itens da pilha
        return len(self._itens)