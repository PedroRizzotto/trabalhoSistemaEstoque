class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nome='{self.nome}', email='{self.email}')"