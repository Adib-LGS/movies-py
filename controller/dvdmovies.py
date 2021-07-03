####Get Only movies in DVD format###

from  .movies import Movies

class DVDMovies(Movies):

	types = "dvd"

	def __init__(self, title, date):
		super().__init__(title, date)
	