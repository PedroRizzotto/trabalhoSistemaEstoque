class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Produto(id_produto={self.id_produto}, nome='{self.nome}', preco={self.preco})"