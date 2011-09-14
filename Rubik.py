# Author Chet Mancini

import os, sys

class Color:
	B = "B"
	W = "W"
	Y = "Y"
	R = "R"
	G = "G"
	O = "O"

class Rubik:

	__moves = 0

	# Representation is stored in a 9-element list
	# 1-3, 4-6, 7-9
	__top = []
	__bottom = []
	__left = []
	__right = []
	__front = []
	__back = []


	def load():
		f = open(sys.args[1], "r")
		# load data structures.		
		f.close()
	
	def solve():
		__moves = 0
		
