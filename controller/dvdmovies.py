####Get Only movies in DVD format###

class DVDMovies(Movies):
	types = "dvd"

	def __init__(self, title, date):
		super().__init__(title, date)
	