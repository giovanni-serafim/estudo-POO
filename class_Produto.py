#estudando encapsulamento com getter e setter

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def desconto(self, percentual):
        self.preço = self.preço - (self.preço * (percentual / 100))    

    #getter, é puxado toda vez que a variavel preço for usada, pois agora preço recebe o valor de preço2 do setter.
    @property
    def preço(self):
        return self.preço2 

    #setter, é puxado quando a variavel preço for inicializada no self.preço = preço, assim ele valida o dado.
    @preço.setter
    def preço(self, valor):
        if isinstance(valor, str): #se valor for uma string...
            valor = float(valor.replace('R$', '')) #remove o R$ e transforma o que sobra em float.
        self.preço2 = valor

p1 = Produto('camiseta', 'R$50')
p1.desconto(50)
print(p1.preço)