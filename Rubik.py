# Author Chet Mancini

import os, sys

# Easy hack for enums. Not terribly pythonic, but will get job done here.
class Color:
	B = "B"
	W = "W"
	Y = "Y"
	R = "R"
	G = "G"
	O = "O"

class Face:
	face = []

	def rotateClock():
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

	def rotateCounter():
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

	paths = []

	# Representation is stored in a 9-element list
	# 1-3, 4-6, 7-9
	top = Face()
	bottom = Face()
	left = Face()
	right = Face()
	front = Face()
	back = Face()
	
	def successors():
		TopCounter = Rubik(self).topCounter()
		TopCounter.paths.push("TCo")

		TopClock = Rubik(self).topClock()
		TopClock.paths.push("TCl")

		LeftForward = Rubik(self).leftForward()
		LeftForward.paths.push("LF")

		LeftBackward = Rubik(self).leftBackward()
		LeftBackward.paths.push("LB")

		RightForward = Rubik(self).rightForward()
		RightForward.paths.push("RF")

		RightBackward = Rubik(self).rightBackward()
		RightBackward.paths.push("RB")

		BottomCounter = Rubik(self).bottomCounter()
		BottomCounter.paths.push("BCo")

		BottomClock = Rubik(self).bottomClock()
		BottomClock.paths.push("BCl")

		FrontClock = Rubik(self).frontClock()
		FrontClock.paths.push("FCl")

		FrontCounter = Rubik(self).frontCounter()
		FrontCounter.paths.push("FCo")

		BackClock = Rubik(self).backClock()
		BackClock.paths.push("BaCl")

		BackCounter = Rubik(self).backCounter()
		BackCounter.paths.push("BaCo")

		return [
			TopCounter, 
			TopClock, 
			LeftForward, 
			LeftBackward, 
			RightForward, 
			RightBackward, 
			BottomCounter, 
			BottomClock, 
			FrontClock, 
			FrontCounter, 
			BackClock, 
			BackCounter,
			]

	def dictKey():
		toReturn = []
		toReturn.append(top.face)
		toReturn.append(bottom.face)
		toReturn.append(left.face)
		toReturn.append(right.face)
		toReturn.append(front.face)
		toReturn.append(back.face)
		return toReturn
	
	def goalCheck():
		return top.allSameColor() 
			and bottom.allSameColor() 
			and left.allSameColor() 
			and right.allSameColor()
			and front.allSameColor()
			and back.allSameColor()

	def topCounter():
		top.rotateCounter()
		temp1 = front.face[0]
		temp2 = front.face[1]
		temp3 = front.face[2]
		front.face[0] = left.face[2]
		front.face[1] = left.face[5]
		front.face[2] = left.face[8]
		left.face[2] = back.face[8]
		left.face[5] = back.face[7]
		left.face[8] = back.face[6]
		back.face[8] = right.face[6]
		back.face[7] = right.face[3]
		back.face[6] = right.face[0]
		right.face[6] = temp1
		right.face[3] = temp2
		right.face[0] = temp3


	def topClock():
		top.rotateClock()
		temp1 = front.face[0]
		temp2 = front.face[1]
		temp3 = front.face[2]
		front.face[0] = right.face[0]
		front.face[1] = right.face[3]
		front.face[2] = right.face[6]
		right.face[0] = back.face[6]
		right.face[3] = back.face[7]
		right.face[6] = back.face[8]
		back.face[6] = left.face[8]
		back.face[7] = left.face[5]
		back.face[8] = left.face[2]		
		left.face[8] = temp3
		left.face[5] = temp2
		left.face[2] = temp1

	def leftForward():
		left.rotateClock()
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
		left.rotateCounter()
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
		right.rotateCounter()
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
		right.rotateClock()
		temp1 = front.face[2]
		temp2 = front.face[5]
		temp3 = front.face[8]
		front.face[2] = bottom.face[2]
		front.face[5] = bottom.face[5]
		front.face[8] = bottom.face[8]
		bottom.face[2] = back.face[2]
		bottom.face[5] = back.face[5]
		bottom.face[8] = back.face[8]
		back.face[2] = top.face[2]
		back.face[5] = top.face[5]
		back.face[8] = top.face[8]
		top.face[2] = temp1
		top.face[5] = temp2
		top.face[8] = temp3
	
	#As Viewed from the TOP
	def bottomCounter():
		bottom.rotateCounter()
		temp1 = front.face[6]
		temp2 = front.face[7]
		temp3 = front.face[8]
		front.face[6] = left.face[0]
		front.face[7] = left.face[3]
		front.face[8] = left.face[6]
		left.face[0] = back.face[2]
		left.face[3] = back.face[1]
		left.face[6] = back.face[0]
		back.face[2] = right.face[8]
		back.face[1] = right.face[5]
		back.face[0] = right.face[2]
		right.face[8] = temp1
		right.face[5] = temp2
		right.face[2] = temp3

	#As View from the TOP
	def bottomClock():
		bottom.rotateClock()
		temp1 = front.face[6]
		temp2 = front.face[7]
		temp3 = front.face[8]
		front.face[6] = right.face[8]
		front.face[7] = right.face[5]
		front.face[8] = right.face[2]
		right.face[8] = back.face[2]
		right.face[5] = back.face[1]
		right.face[2] = back.face[0]
		back.face[2] = left.face[0]
		back.face[1] = left.face[3]
		back.face[0] = left.face[6]
		left.face[0] = temp1
		left.face[3] = temp2
		left.face[6] = temp3
	
	def frontClock():
		front.rotateClock()
		temp1 = top.face[6]
		temp2 = top.face[7]
		temp3 = top.face[8]
		top.face[6] = left.face[6]
		top.face[7] = left.face[7]
		top.face[8] = left.face[8]
		left.face[6] = bottom.face[2]
		left.face[7] = bottom.face[1]
		left.face[8] = bottom.face[0]
		bottom.face[2] = right.face[6]
		bottom.face[1] = right.face[7]
		bottom.face[0] = right.face[8]
		right.face[6] = temp1
		right.face[7] = temp2
		right.face[8] = temp3

	def frontCounter():
		front.rotateCounter()
		temp1 = top.face[6]
		temp2 = top.face[7]
		temp3 = top.face[8]
		top.face[6] = right.face[6]
		top.face[7] = right.face[7]
		top.face[8] = right.face[8]
		right.face[6] = bottom.face[2]
		right.face[7] = bottom.face[1]
		right.face[8] = bottom.face[0]
		bottom.face[2] = left.face[6] 
		bottom.face[1] = left.face[7]
		bottom.face[0] = left.face[8]
		left.face[6] = temp1
		left.face[7] = temp2
		left.face[8] = temp3
	
	def backClock():
		back.rotateCounter()
		temp1 = top.face[0]
		temp2 = top.face[1]
		temp3 = top.face[2]
		top.face[0] = left.face[0]
		top.face[1] = left.face[1]
		top.face[2] = left.face[2]
		left.face[0] = bottom.face[6]
		left.face[1] = bottom.face[7]
		left.face[2] = bottom.face[8]
		bottom.face[6] = right.face[2]
		bottom.face[7] = right.face[1]
		bottom.face[8] = right.face[0]
		right.face[2] = temp3
		right.face[1] = temp2
		right.face[0] = temp1


	def backCounter():
		back.rotateClock()
		temp1 = top.face[0]
		temp2 = top.face[1]
		temp3 = top.face[2]
		top.face[0] = right.face[0]
		top.face[1] = right.face[1]
		top.face[2] = right.face[2]
		right.face[0] = bottom.face[8]
		right.face[1] = bottom.face[7]
		right.face[2] = bottom.face[6]
		bottom.face[8] = left.face[2]
		bottom.face[7] = left.face[1]
		bottom.face[6] = left.face[0]
		left.face[2] = temp3
		left.face[1] = temp2
		left.face[0] = temp1



class Solver:
	Cube = Rubik()

	def readFace(face, f):
		line1 = f.readLine().split()
		line2 = f.readLine().split()
		line3 = f.readLine().split()
		face = line1
		face[3] = line2[0]
		face[4] = line2[1]
		face[5] = line2[2]
		face[6] = line3[0]
		face[7] = line3[1]
		face[8] = line4[2]

	def load():
		f = open(sys.argv[1], "r")
		readFace(Cube.back, f)
		readFace(Cube.left, f)
		readFace(Cube.top, f)
		readFace(Cube.right, f)
		readFace(Cube.front, f)
		readFace(Cube.bottom, f)
		f.close()

	# Main Algorithm
	def solve():
		load()
		openList = Cube.successors()
		closeList = {}
		moves = 0
		while True:
			newCube = openList.pop()
			if closeList.hasKey(newCube.dictKey()) or (len(newCube.paths) == 20):
				continue
			else:
				closeList[newCube.dictKey()] = newCube

			if newCube.goalCheck():
				return ", ".join(newCube.paths)
			else:
				for cube in newCube.successors():
					if !closeList.hasKey(cube.dictKey()):
						openList.push(cube)
			if len(openList) == 0:
				break
			return "failure"


##################
### Run ##########
DoIt = Solver()
DoIt.solve()






		
