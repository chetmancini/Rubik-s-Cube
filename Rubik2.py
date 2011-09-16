# Author Chet Mancini
# Disclaimer - this code needs a lot of work.
# There's a lot that can be refactored at the moment!
# I just had to get it working for class.
import sys, copy


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

    def rotateClock(self):
        temp = self.face
        temp[0] = self.face[6]
        temp[1] = self.face[3]
        temp[2] = self.face[0]
        temp[3] = self.face[7]
        #faceClone[4] = face[4] (always static)
        temp[5] = self.face[1]
        temp[6] = self.face[8]
        temp[7] = self.face[5]
        temp[8] = self.face[2]
        self.face = temp

    def rotateCounter(self):
        temp = self.face
        temp[0] = self.face[2]
        temp[1] = self.face[5]
        temp[2] = self.face[8]
        temp[3] = self.face[1]
        #faceClone[4] = face[4] (always static)
        temp[5] = self.face[7]
        temp[6] = self.face[0]
        temp[7] = self.face[3]
        temp[8] = self.face[6]
        self.face = temp
    
    def allSameColor():
        color = face[0]
        for test in face:
            if test != color:
                return False
        return True

class Rubik:

    paths = []

    top = Face()
    bottom = Face()
    left = Face()
    right = Face()
    front = Face()
    back = Face()

    # Representation is stored in a 9-element list
    # 1-3, 4-6, 7-9
    def __init__(self):
        paths = []
    
    def successors(self):
        toReturn = []
        TopCounter = copy.deepcopy(self)
        topCounter(TopCounter)
        TopCounter.paths.append("TCo")
        toReturn.append(TopCounter)
        
        TopClock = copy.deepcopy(self)
        topClock(TopClock)
        TopClock.paths.append("TCl")
        toReturn.append(TopClock)

#         LeftForward = copy.deepcopy(self)
#         LeftForward.leftForward()
#         LeftForward.paths.append("LF")
#         toReturn.append(LeftForward)
# 
#         LeftBackward = copy.deepcopy(self)
#         LeftBackward.leftBackward()
#         LeftBackward.paths.append("LB")
#         toReturn.append(LeftBackward)
# 
#         RightForward = copy.deepcopy(self)
#         RightForward.rightForward()
#         RightForward.paths.append("RF")
#         toReturn.append(RightForward)
# 
#         RightBackward = copy.deepcopy(self)
#         RightBackward.rightBackward()
#         RightBackward.paths.append("RB")
#         toReturn.append(RightBackward)
# 
#         BottomCounter = copy.deepcopy(self)
#         BottomCounter.bottomCounter()
#         BottomCounter.paths.append("BCo")
#         toReturn.append(BottomCounter)
# 
#         BottomClock = copy.deepcopy(self)
#         BottomClock.bottomClock()
#         BottomClock.paths.append("BCl")
#         toReturn.append(BottomClock)
# 
#         FrontClock = copy.deepcopy(self)
#         FrontClock.frontClock()
#         FrontClock.paths.append("FCl")
#         toReturn.append(FrontClock)
# 
#         FrontCounter = copy.deepcopy(self)
#         FrontCounter.frontCounter()
#         FrontCounter.paths.append("FCo")
#         toReturn.append(FrontCounter)
#         print FrontCounter.dictKey()
# 
#         BackClock = copy.deepcopy(self)
#         BackClock.backClock()
#         BackClock.paths.append("BaCl")
#         toReturn.append(BackClock)
#         print BackClock.dictKey()
# 
#         BackCounter = copy.deepcopy(self)
#         BackCounter.backCounter()
#         BackCounter.paths.append("BaCo")
#         toReturn.append(BackCounter)
#         print BackCounter.dictKey()
        return toReturn
        

    def dictKey(self):
        toReturn = []
        toReturn.extend(self.top.face)
        toReturn.extend(self.bottom.face)
        toReturn.extend(self.left.face)
        toReturn.extend(self.right.face)
        toReturn.extend(self.front.face)
        toReturn.extend(self.back.face)
        return ''.join(toReturn)
    
    def goalCheck():
        return top.allSameColor() and bottom.allSameColor() and left.allSameColor() and right.allSameColor() and front.allSameColor() and back.allSameColor()


class RubikCube:

    def solve(self):
        Cube = Rubik()
        f = open(sys.argv[1], "r")
        #Tried to refactor this but got a bunch of global var errors? weird.
        Cube.back.face = f.readline().split()
        Cube.back.face.extend(f.readline().split())
        Cube.back.face.extend(f.readline().split())
        Cube.left.face = f.readline().split()
        Cube.left.face.extend(f.readline().split())
        Cube.left.face.extend(f.readline().split())
        Cube.top.face = f.readline().split()
        Cube.top.face.extend(f.readline().split())
        Cube.top.face.extend(f.readline().split())
        Cube.right.face = f.readline().split()
        Cube.right.face.extend(f.readline().split())
        Cube.right.face.extend(f.readline().split())
        Cube.front.face = f.readline().split()
        Cube.front.face.extend(f.readline().split())
        Cube.front.face.extend(f.readline().split())
        Cube.bottom.face = f.readline().split()
        Cube.bottom.face.extend(f.readline().split())
        Cube.bottom.face.extend(f.readline().split())
        f.close()
        openList = Cube.successors()
        closeList = {}
        closeList[Cube.dictKey()] = Cube
        while len(openList) > 0:
            newCube = openList.pop()
            print newCube.dictKey()
            if closeList.has_key(newCube.dictKey()) or (len(newCube.paths) == 20):
                continue
            else:
                closeList[newCube.dictKey()] = newCube
                
            if newCube.goalCheck():
                return ', '.join(newCube.paths)
            else:
                for successor in newCube.successors():
                    if not closeList.has_key(successor.dictKey()):
                        openList.append(successor)
        return 'Done'


### Transformations ####
def topCounter(cube):
	cube.top.rotateCounter()
	temp1 = cube.front.face[0]
	temp2 = cube.front.face[1]
	temp3 = cube.front.face[2]
	cube.front.face[0] = cube.left.face[2]
	cube.front.face[1] = cube.left.face[5]
	cube.front.face[2] = cube.left.face[8]
	cube.left.face[2] = cube.back.face[8]
	cube.left.face[5] = cube.back.face[7]
	cube.left.face[8] = cube.back.face[6]
	cube.back.face[8] = cube.right.face[6]
	cube.back.face[7] = cube.right.face[3]
	cube.back.face[6] = cube.right.face[0]
	cube.right.face[6] = temp1
	cube.right.face[3] = temp2
	cube.right.face[0] = temp3

def topClock(cube):
	cube.top.rotateClock()
	temp1 = cube.front.face[0]
	temp2 = cube.front.face[1]
	temp3 = cube.front.face[2]
	cube.front.face[0] = cube.right.face[0]
	cube.front.face[1] = cube.right.face[3]
	cube.front.face[2] = cube.right.face[6]
	cube.right.face[0] = cube.back.face[6]
	cube.right.face[3] = cube.back.face[7]
	cube.right.face[6] = cube.back.face[8]
	cube.back.face[6] = cube.left.face[8]
	cube.back.face[7] = cube.left.face[5]
	cube.back.face[8] = cube.left.face[2]       
	cube.left.face[8] = temp3
	cube.left.face[5] = temp2
	cube.left.face[2] = temp1

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


if __name__=="__main__":    
    c = RubikCube()
    print c.solve()
