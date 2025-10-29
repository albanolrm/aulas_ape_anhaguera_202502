from classes import Aluno
from classes import Produto
from classes import Carro

aluno1 = Aluno("Maria", 20)
aluno2 = Aluno("João", 22)

aluno1.adicionar_nota(8.5)
aluno1.adicionar_nota(7.0)
aluno2.adicionar_nota(9.0)

print(aluno1.nome, aluno1.calcular_media())  # Maria 7.75
print(aluno2.nome, aluno2.calcular_media())  # João 9.0

"""
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.mostrar_status()

meu_carro.ligar()
meu_carro.mostrar_status()

meu_carro.desligar()
meu_carro.mostrar_status()

p1 = Produto("Caneta", 2.50, 10)
p2 = Produto("Caderno", 15.90, 3)

p1.mostrar_informacoes()
print()  # linha em branco
p2.mostrar_informacoes("
"""