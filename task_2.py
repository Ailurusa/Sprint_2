class Movies:
    genre = ''

    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'{self.genre}: {self.movies}'


class Comedy(Movies):
    genre = 'Комедии'


class Drama(Movies):
    genre = 'Драмы'


comedy = Comedy()
print(comedy.add_movie('Большой куш'))

drama = Drama()
print(drama.add_movie('Оружейный барон'))
