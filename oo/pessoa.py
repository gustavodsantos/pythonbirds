class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    gustavo = Pessoa(nome='Gustavo')
    greyce = Pessoa(gustavo, nome='Greyce')
    print(Pessoa.cumprimentar(greyce))
    print(id(greyce))
    print(greyce.cumprimentar())
    print(greyce.nome)
    print(greyce.idade)
    for filho in greyce.filhos:
        print(filho.nome)
    greyce.sobrenome = 'Santos'
    del greyce.filhos
    print(greyce.__dict__)
    print(gustavo.__dict__)

