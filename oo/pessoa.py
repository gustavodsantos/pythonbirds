class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    gustavo = Homem(nome='Gustavo')
    greyce = Homem(gustavo, nome='Greyce')
    print(Pessoa.cumprimentar(greyce))
    print(id(greyce))
    print(greyce.cumprimentar())
    print(greyce.nome)
    print(greyce.idade)
    for filho in greyce.filhos:
        print(filho.nome)
    greyce.sobrenome = 'Santos'
    del greyce.filhos
    greyce.olhos = 1
    del greyce.olhos
    print(greyce.__dict__)
    print(gustavo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(greyce.olhos)
    print(gustavo.olhos)
    print(id(Pessoa.olhos), id(greyce.olhos), id(gustavo.olhos))
    print(Pessoa.metodo_estatico(), greyce.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), greyce.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(gustavo, Pessoa))
    print(isinstance(gustavo, Homem))
