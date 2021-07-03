####Get Only movies in DVD format###

class DVDMovies(Movies):

	def __init__(self, name, creation_date, location, type = « DVD » ):
	super().__init__( name, creation_date, location, type)
	
	def get_only_dvd_movie(self):