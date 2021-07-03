### My library

import random
from .movies import Movies
from .sortmovies import SortMovies
from model.data import films

class Library:

    def __init__(self):

        self.movie_list = []
        for movie_data in films:
            movie = SortMovies(movie_data).extract_movie_from_data()
            movie.where = self
            self.movie_list.append(movie)

        self.sort_by_date_and_name()

    def sort_by_date_and_name(self):
        self.movie_list.sort(key=lambda movie: (movie.date, movie.name))

    def sort_by_type(self):
        self.movie_list.sort(key=lambda movie: (movie.types))

    def get_random_movie(self):
        return random.choice(self.movie_list)

    def find_movie_by_name(self):
        for movie in self.movie_list:
            if name == movie.name:
                return movie
        return None