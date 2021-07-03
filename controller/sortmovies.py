###Sort movies by type name and date to Generate It ###

from .movies import Movies
from .dvdmovies import DVDMovies
from .vhfmovies import VHFMovies

class SortMovies():

	NAME_AND_DATE_INDEX = 0
	TYPE_INDEX = 1

	def __init__(self, movie_data):
		self.movie_data = movie_data

	def extract_movie_from_data(self):
		name = self.generate_name_movies()
		date = self.generate_date_movies()
		types = self.generate_movies_by_type()

		# Oterate on class tuple
		for Movies in (DVDMovies, VHFMovies):
			if types == Movies.types:
				return Movies(title, date)
				
	
	def generate_movies_by_type(self):
		return self.movie_data[self.TYPE_INDEX].lower()


	def generate_name_movies(self):
		name_date = self.movie_data[self.NAME_AND_DATE_INDEX]
		return name_date[: name_date.index("(")].strip()

	def generate_date_movies(self):
		name_date = self.movie_data[self.NAME_AND_DATE_INDEX]
		date_in_parenthesis = name_date[name_date.index("(") :]
		date_letters = date_in_parenthesis.replace("(", "").replace(")", "")
		return int(date_letters)