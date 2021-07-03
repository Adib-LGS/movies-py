###Get movies from data list####

class Movies:

	def __init__(self, title, creation_date, types):
		self.title = title
		self.creation_date = creation_date
		self.types = types
		self.movies_in_list = []


	def add_movies_in_list(self):
		movie_list = self.movies_in_list
		movie_list.extend([self.title, self.creation_date, self.types])
		return movie_list

	
	def get_random_movie_in_list(self):
		pass


	def get_other_user_movie(self):
		pass