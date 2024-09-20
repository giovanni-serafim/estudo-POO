from datetime import datetime

class Pessoa:

    ano_atual = int (datetime.strftime(datetime.now(), '%Y'))


    def __init__(self, nome, idade, comendo=False, falando = False, ):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    
    @classmethod
    def por_ano_nascimento (cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        

    def get_ano_nacimento (self):
        print ('ano de nascimento: ', self.ano_atual - self.idade)    

    
    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} ja está comendo')
            return
        if self.falando:
            print(f'{self.nome} não pode comer pois está falando')
            return
        print(f'{self.nome} está comendo {comida}')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False


    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} ja está falando')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar pois está comendo')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não entá falando')
        print(f'{self.nome} parou de falar')
        self.falando = False
 

