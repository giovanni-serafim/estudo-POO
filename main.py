from class_Pessoa import Pessoa

#p1 = Pessoa('marcos', 19)

#p1.get_ano_nacimento()

p1 = Pessoa.por_ano_nascimento('luiz', 1987)

print(p1.idade)

p1.falar('video game')
p1.comer('pizza')
p1.parar_falar()
p1.comer('pizza')

