# Trabalho Avaliativo POO - Sistema de Controle de Estoque

**Disciplina:** Organização e Abstração na Programação

## Integrantes

Carlos Eduardo Zanin - 1138275

Eduarda de Quevedo Ferreira Bolner - 1137825

João Vitor da Silva - 1138170

Pedro Henrique Moreschi Rizzotto - 1138024

## Descrição do sistema

Esse é um sistema de estoque desenvolvido em python e é executado no terminal. Todos os dados são salvos automaticamente em arquivos CSV. O Sistema tem as seguintes funcionalidades:

#### Funcionalidades

1. Cadastrar Cliente
2. Listar clientes
3. Cadastrar produto
4. Listar produtos do estoque
5. Pesquisar produto por nome ou ID
6. Realizar venda
7. Visualizar fila de vendas
8. Desfazer ultima operacao
9. Exibir valor total do estoque
10. Exibir valor total de vendas realizadas
11. Exibir clientes e valores totais gastos
12. Sair

## Estruturas de Dados

Nesse sistema foram utilizadas as seguintes estruturas de dados:

- Lista simplesmente encadeada: Usada para armazenar os clientes e os produtos de estoque.

- Fila: Usada pra registrar as vendas usando a lógica FIFO para garantir que os dados vão ser guardados na ordem que aconteceram.

- Pilha: Usada pra guardar o histórico do que foi feito e possibilitar desfazer uma ação. Essa estrutura segue a lógica LIFO.

## Persistência automática

O sistema salva os dados automaticamente ao fazer um ação em 3 arquivos .csv (escolhemos .csv porque o professor comentou que já nos traria um pouco de lógica pra matéria de banco de dados)

- clientes.csv
- produtos.csv
- vendas.csv

Se os arquivos não existirem, eles serão criados quando precisar salvar algo.

## Como executar o projeto?

1. Instale o Python
2. Clone o repositório: git clone https://github.com/PedroRizzotto/trabalhoSistemaEstoque.git
3. Entre na pasta do projeto
4. Execute `python main.py` no terminal
