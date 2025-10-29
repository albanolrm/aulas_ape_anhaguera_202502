class Aluno:
    # Método construtor: define o que o aluno "tem"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []

    # Método: define o que o aluno "faz"
    def adicionar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

    def mostrar_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço unitário: R$ {self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Total: R$ {self.calcular_total():.2f}")

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False  # começa desligado

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} foi ligado.")
        else:
            print(f"{self.modelo} já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.modelo} foi desligado.")
        else:
            print(f"{self.modelo} já estava desligado.")

    def mostrar_status(self):
        estado = "ligado" if self.ligado else "desligado"
        print(f"Carro: {self.marca} {self.modelo} ({self.ano}) está {estado}.")