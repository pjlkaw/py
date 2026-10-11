carrinhoArray = []

class Product: 
    def __init__(self, nome, valor, marca, descricao):
        self.nome = nome
        self.valor = valor
        self.marca = marca
        self.descricao = descricao

    def verMais(self):
        print(self.nome, self.valor, self.marca, self.descricao)

class shoppingCart:
    def __init__(self):
        self.produtos = []

    def produtoCarrinho(self, produto):
        self.produtos.append(produto)

    def mostrarCarrinho(self):
        for produto in self.produtos:
            print(" - ", produto.nome, produto.valor, produto.marca, produto.descricao, "\n")

    def calcularTotal(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        print(total)

carrinho = shoppingCart()

carrinho.produtoCarrinho(Product('Fone De Ouvido Headset', 167, 'Havit', 'Headset Gamer Havit H2002D Aparência e textura proporcionais, simples e generosas.'))
carrinho.produtoCarrinho(Product('Mouse Gamer', 99, 'Redragon', 'Mouse Gamer Redragon M601 RGB 7200 DPI 7 Botões Programáveis.'))
carrinho.produtoCarrinho(Product('Teclado Mecânico', 299, 'HyperX', 'Teclado Mecânico HyperX Alloy FPS Pro Switches CHERRY MX Red.'))
carrinho.produtoCarrinho(Product('Monitor Gamer', 899, 'Samsung', 'Monitor Gamer Samsung Odyssey G5 27" Curvo 165Hz 1ms FreeSync Premium.'))

carrinho.mostrarCarrinho()

carrinho.calcularTotal()
