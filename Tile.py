import os, random, time
from namegen import name_cvcv, name_cvcvc, name_gen

class Tile():

	def __init__(self, x, y):
		if x is 0: #call factory methods
			self.location_x = 0
			self.location_y = 0
		else:
			self.location_x = x
			self.location_y = y
		                
		self.symbol = "-"
		

	def set_kelp(self):
		self.symbol = "K"	

	def set_food(self):
		self.symbol = "#"
