###Get only movies in VHF format####

class VHFMovies(Movies):
    
	def __init__(self, name, creation_date, location, type = « VHF » ):
	super().__init__( name, creation_date, location, type)
	
	def get_only_vhf_movie(self):