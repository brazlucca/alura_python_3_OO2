class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes'

#####---_#####    MAIN    #####----#####

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
a_origem = Filme('a origem', 2014, 210)
house_of_cards = Serie('sons of anarchy', 2018, 3)
band_of_brothers = Serie('band of brothers', 2004, 1)

vingadores.dar_like()
a_origem.dar_like()
a_origem.dar_like()
a_origem.dar_like()
a_origem.dar_like()

house_of_cards.dar_like()
house_of_cards.dar_like()
band_of_brothers.dar_like()
band_of_brothers.dar_like()
band_of_brothers.dar_like()
band_of_brothers.dar_like()
band_of_brothers.dar_like()

print()
print()

filmes_e_series = [house_of_cards, band_of_brothers, a_origem]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Nome da playlist: {playlist_fim_de_semana.nome}')
print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
print()
for programa in playlist_fim_de_semana:
    print(programa)

print()

len(playlist_fim_de_semana)