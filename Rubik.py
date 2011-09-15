# Author Chet Mancini

import os, sys

class Color:
	B = "B"
	W = "W"
	Y = "Y"
	R = "R"
	G = "G"
	O = "O"

class Face:
	face = []

	def rotateRight():
		temp = face
		temp[0] = face[6]
		temp[1] = face[3]
		temp[2] = face[0]
		temp[3] = face[7]
		#faceClone[4] = face[4] (always static)
		temp[5] = face[1]
		temp[6] = face[8]
		temp[7] = face[5]
		temp[8]	= face[2]
		face = temp

	def rotateLeft():
		temp = face
		temp[0] = face[2]
		temp[1] = face[5]
		temp[2] = face[8]
		temp[3] = face[1]
		#faceClone[4] = face[4] (always static)
		temp[5] = face[7]
		temp[6] = face[0]
		temp[7] = face[3]
		temp[8]	= face[6]
		face = temp
	
	def allSameColor():
		color = face[0]
		for test in face:
			if test != color:
				return False
		return True


class Rubik:

	__moves = 0

	# Representation is stored in a 9-element list
	# 1-3, 4-6, 7-9
	top = Face()
	bottom = Face()
	left = Face()
	right = Face()
	front = Face()
	back = Face()


	def load():
		f = open(sys.args[1], "r")
		# load data structures.		
		f.close()

	def swap(v1, v2):
		temp = v1
		v1 = v2
		v2 = temp
	
	def threeSwap()
	
	def goalCheck():
		return top.allSameColor() 
			and bottom.allSameColor() 
			and left.allSameColor() 
			and right.allSameColor()
			and front.allSameColor()
			and back.allSameColor()

	def topLeft():
		top.rotateLeft()
		temp1 = front.face[0]
		temp2 = front.face[1]
		temp3 = front.face[2]
		front.face[0] = left.face[2]
		front.face[1] = left.face[5]
		front.face[2] = left.face[8]
		left.face[2] = back.face[8]
		left.face[5] = back.face[7]
		left.face[8] = back.face[6]
		back.face[6] = right.face[0]
		back.face[7] = right.face[3]
		back.face[8] = right.face[6]
		right.face[0] = temp3
		right.face[3] = temp2
		right.face[6] = temp1


	def topRight():
		top.rotateRight()
		temp1 = front.face[0]
		temp2 = front.face[1]
		temp3 = front.face[2]
		front.face[0] = right.face[0]
		front.face[1] = right.face[6]
		front.face[2] = right.face[6]
		right.face[0] = back.face[6]
		right.face[3] = back.face[7]
		right.face[6] = back.face[8]
		back.face[6] = left.face[8]
		back.face[7] = left.face[5]
		back.face[8] = left.face[2]		
		left.face[2] = back.face[8]
		left.face[5] = back.face[7]
		left.face[8] = back.face[6]

	def leftForward():
		left.rotateRight()
		temp1 = front.face[0]
		temp2 = front.face[3]
		temp3 = front.face[6]
		front.face[0] = top.face[0]
		front.face[3] = top.face[3]
		front.face[6] = top.face[6]
		top.face[0] = back.face[0]
		top.face[3] = back.face[3]
		top.face[6] = back.face[6]
		back.face[0] = bottom.face[0]
		back.face[3] = bottom.face[3]
		back.face[6] = bottom.face[6]
		bottom.face[0] = temp1
		bottom.face[3] = temp2
		bottom.face[6] = temp3

	
	def leftBackward():
		left.rotateLeft()
		temp1 = front.face[0]
		temp2 = front.face[3]
		temp3 = front.face[6]
		front.face[0] = bottom.face[0]
		front.face[3] = bottom.face[3]
		front.face[6] = bottom.face[6]
		bottom.face[0] = back.face[0]
		bottom.face[3] = back.face[3]
		bottom.face[6] = back.face[6]
		back.face[0] = top.face[0]
		back.face[3] = top.face[3]
		back.face[6] = top.face[6]
		top.face[0] = temp1
		top.face[3] = temp2
		top.face[6] = temp3

	def rightForward():
		right.rotateLeft()
		temp1 = front.face[2]
		temp2 = front.face[5]
		temp3 = front.face[8]
		front.face[2] = top.face[2]
		front.face[5] = top.face[5]
		front.face[8] = top.face[8]
		top.face[2] = back.face[2]
		top.face[5] = back.face[5]
		top.face[8] = back.face[8]
		back.face[2] = bottom.face[2]
		back.face[5] = bottom.face[5]
		back.face[8] = bottom.face[8]
		bottom.face[2] = temp1
		bottom.face[5] = temp2
		bottom.face[8] = temp3
	
	def rightBackward():
		right.rotateRight()
		#TODO

	def bottomLeft():
		bottom.rotateLeft()
		#TODO
	
	def bottomRight():
		bottom.rotateRight()
		#TODO
	
	def frontRight():
		front.rotateRight()
		#TODO

	def frontLeft():
		front.rotateLeft()
		#TODO
	
	def backRight():
		back.rotateLeft()
		#TODO

	def backLeft():
		back.rotateRight()
		#TODO

	# Main Algorithm
	def solve():
		__moves = 0
		
