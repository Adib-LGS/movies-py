###Sort movies by type name and date to Generate It ###

from controller.movies import Movies
from controller.movies import DVDMovies
from controller.movies import VHFMovies

class SortMovies():

	NAME_AND_DATE_INDEX = 0
	TYPE_INDEX = 1

	def __init__(self, movie_data):
		self.movie_data = movie_data

	def extract_movie_from_data(self):
		name = self.generate_name()
		date = self.generate_date()
		types = self.generate_type()

		# Oterate on class tuple
		for Movies in (DVDMovies, VHFMovies):
			if types == Movies.types:
				return Movies(name, date)
	
	def generate_movies_by_type(self):
		return self.movie_data[self.TYPE_INDEX].lower()

	def generate_name_movies(self):
		name_date = self.movie_data[self.NAME_AND_DATE_INDEX].strip()

	def generate_date_movies(self):
		name_date = self.movie_data[self.NAME_AND_DATE_INDEX].strip()
		date_in_parenthesis = name_date[name_date.index("(") :]
        date_letters = date_in_parenthesis.replace("(", "").replace(")", "")
        return int(date_letters)