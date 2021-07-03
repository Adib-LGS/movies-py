###Get only movies in VHF format####

class VHFMovies(Movies):

    types = "VHF"
	 
	def __init__(self, title, date):
	super().__init__( title, date)
	