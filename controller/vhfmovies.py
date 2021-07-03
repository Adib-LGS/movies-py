#coding:utf-8

###Get only movies in VHF format####
from .movies import Movies

class VHFMovies(Movies):

	types = "vhf"
	
	def __init__(self, title, date):
		super().__init__(title, date)
		self.magnetic_tape = True
	
	