# Author Chet Mancini
#
#
# Input: 3x54 matrix, columns are seperated vertically by spaces.
# W Y B
# G Y R
# R O B
# ...
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
    #List to store the color values
    # Representation is stored in a 9-element list
    # 1-3, 4-6, 7-9
    face = []

    # Rotate a face clockwise
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

    # Rotate a face counter-clockwise
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
    
    # Are all the pieces on the face the same color? If so, we can use this to check
    # for a goal state.
    def allSameColor():
        color = face[0]
        for test in face:
            if test != color:
                return False
        return True

# The Cube
class Rubik:
    # States taken so far, on a stack
    paths = []

    # The faces on the cube.
    top = Face()
    bottom = Face()
    left = Face()
    right = Face()
    front = Face()
    back = Face()

	# Constructor
    def __init__(self):
        paths = []
    
    # Successor Function
    def successors(self):
        toReturn = []
        TopCounter = copy.deepcopy(self)
        TopCounter.topCounter()
        TopCounter.paths.append("TCo")
        toReturn.append(TopCounter)
        
        TopClock = copy.deepcopy(self)
        TopClock.topClock()
        TopClock.paths.append("TCl")
        toReturn.append(TopClock)

        LeftForward = copy.deepcopy(self)
        LeftForward.leftForward()
        LeftForward.paths.append("LF")
        toReturn.append(LeftForward)

        LeftBackward = copy.deepcopy(self)
        LeftBackward.leftBackward()
        LeftBackward.paths.append("LB")
        toReturn.append(LeftBackward)

        RightForward = copy.deepcopy(self)
        RightForward.rightForward()
        RightForward.paths.append("RF")
        toReturn.append(RightForward)

        RightBackward = copy.deepcopy(self)
        RightBackward.rightBackward()
        RightBackward.paths.append("RB")
        toReturn.append(RightBackward)

        BottomCounter = copy.deepcopy(self)
        BottomCounter.bottomCounter()
        BottomCounter.paths.append("BCo")
        toReturn.append(BottomCounter)

        BottomClock = copy.deepcopy(self)
        BottomClock.bottomClock()
        BottomClock.paths.append("BCl")
        toReturn.append(BottomClock)

        FrontClock = copy.deepcopy(self)
        FrontClock.frontClock()
        FrontClock.paths.append("FCl")
        toReturn.append(FrontClock)

        FrontCounter = copy.deepcopy(self)
        FrontCounter.frontCounter()
        FrontCounter.paths.append("FCo")
        toReturn.append(FrontCounter)

        BackClock = copy.deepcopy(self)
        BackClock.backClock()
        BackClock.paths.append("BaCl")
        toReturn.append(BackClock)

        BackCounter = copy.deepcopy(self)
        BackCounter.backCounter()
        BackCounter.paths.append("BaCo")
        toReturn.append(BackCounter)
        return toReturn
        
    # String representation of the cube. Good for closed list as well as debugging.
    def dictKey(self):
        toReturn = []
        toReturn.extend(self.top.face)
        toReturn.extend(self.bottom.face)
        toReturn.extend(self.left.face)
        toReturn.extend(self.right.face)
        toReturn.extend(self.front.face)
        toReturn.extend(self.back.face)
        return ''.join(toReturn)
    
    # Check if we have reached the goal state.
    def goalCheck():
        return top.allSameColor() and bottom.allSameColor() and left.allSameColor() and right.allSameColor() and front.allSameColor() and back.allSameColor()

	# Rotate the top counterclockwise.
    def topCounter(self):
        self.top.rotateCounter()
        temp1 = self.front.face[0]
        temp2 = self.front.face[1]
        temp3 = self.front.face[2]
        self.front.face[0] = self.left.face[2]
        self.front.face[1] = self.left.face[5]
        self.front.face[2] = self.left.face[8]
        self.left.face[2] = self.back.face[8]
        self.left.face[5] = self.back.face[7]
        self.left.face[8] = self.back.face[6]
        self.back.face[8] = self.right.face[6]
        self.back.face[7] = self.right.face[3]
        self.back.face[6] = self.right.face[0]
        self.right.face[6] = temp1
        self.right.face[3] = temp2
        self.right.face[0] = temp3


    # Rotate the top clockwise.
    def topClock(self):
        self.top.rotateClock()
        temp1 = self.front.face[0]
        temp2 = self.front.face[1]
        temp3 = self.front.face[2]
        self.front.face[0] = self.right.face[0]
        self.front.face[1] = self.right.face[3]
        self.front.face[2] = self.right.face[6]
        self.right.face[0] = self.back.face[6]
        self.right.face[3] = self.back.face[7]
        self.right.face[6] = self.back.face[8]
        self.back.face[6] = self.left.face[8]
        self.back.face[7] = self.left.face[5]
        self.back.face[8] = self.left.face[2]       
        self.left.face[8] = temp3
        self.left.face[5] = temp2
        self.left.face[2] = temp1

    # Rotate the left forward (towards you)
    def leftForward(self):
        self.left.rotateClock()
        temp1 = self.front.face[0]
        temp2 = self.front.face[3]
        temp3 = self.front.face[6]
        self.front.face[0] = self.top.face[0]
        self.front.face[3] = self.top.face[3]
        self.front.face[6] = self.top.face[6]
        self.top.face[0] = self.back.face[0]
        self.top.face[3] = self.back.face[3]
        self.top.face[6] = self.back.face[6]
        self.back.face[0] = self.bottom.face[0]
        self.back.face[3] = self.bottom.face[3]
        self.back.face[6] = self.bottom.face[6]
        self.bottom.face[0] = temp1
        self.bottom.face[3] = temp2
        self.bottom.face[6] = temp3

    # Rotate the left backwards (away from you)
    def leftBackward(self):
        self.left.rotateCounter()
        temp1 = self.front.face[0]
        temp2 = self.front.face[3]
        temp3 = self.front.face[6]
        self.front.face[0] = self.bottom.face[0]
        self.front.face[3] = self.bottom.face[3]
        self.front.face[6] = self.bottom.face[6]
        self.bottom.face[0] = self.back.face[0]
        self.bottom.face[3] = self.back.face[3]
        self.bottom.face[6] = self.back.face[6]
        self.back.face[0] = self.top.face[0]
        self.back.face[3] = self.top.face[3]
        self.back.face[6] = self.top.face[6]
        self.top.face[0] = temp1
        self.top.face[3] = temp2
        self.top.face[6] = temp3

    # Rotate the right side forwards (towards you)
    def rightForward(self):
        self.right.rotateCounter()
        temp1 = self.front.face[2]
        temp2 = self.front.face[5]
        temp3 = self.front.face[8]
        self.front.face[2] = self.top.face[2]
        self.front.face[5] = self.top.face[5]
        self.front.face[8] = self.top.face[8]
        self.top.face[2] = self.back.face[2]
        self.top.face[5] = self.back.face[5]
        self.top.face[8] = self.back.face[8]
        self.back.face[2] = self.bottom.face[2]
        self.back.face[5] = self.bottom.face[5]
        self.back.face[8] = self.bottom.face[8]
        self.bottom.face[2] = temp1
        self.bottom.face[5] = temp2
        self.bottom.face[8] = temp3
    
    # Rotate the right side backwards (away from you)
    def rightBackward(self):
        self.right.rotateClock()
        temp1 = self.front.face[2]
        temp2 = self.front.face[5]
        temp3 = self.front.face[8]
        self.front.face[2] = self.bottom.face[2]
        self.front.face[5] = self.bottom.face[5]
        self.front.face[8] = self.bottom.face[8]
        self.bottom.face[2] = self.back.face[2]
        self.bottom.face[5] = self.back.face[5]
        self.bottom.face[8] = self.back.face[8]
        self.back.face[2] = self.top.face[2]
        self.back.face[5] = self.top.face[5]
        self.back.face[8] = self.top.face[8]
        self.top.face[2] = temp1
        self.top.face[5] = temp2
        self.top.face[8] = temp3
    
    # Rotate the bottom counter clockwise (as viewed from the perspective of the top)
    def bottomCounter(self):
        self.bottom.rotateCounter()
        temp1 = self.front.face[6]
        temp2 = self.front.face[7]
        temp3 = self.front.face[8]
        self.front.face[6] = self.left.face[0]
        self.front.face[7] = self.left.face[3]
        self.front.face[8] = self.left.face[6]
        self.left.face[0] = self.back.face[2]
        self.left.face[3] = self.back.face[1]
        self.left.face[6] = self.back.face[0]
        self.back.face[2] = self.right.face[8]
        self.back.face[1] = self.right.face[5]
        self.back.face[0] = self.right.face[2]
        self.right.face[8] = temp1
        self.right.face[5] = temp2
        self.right.face[2] = temp3

    # Rotate the bottom clockwise, (as viewed from the perspective of the top)
    def bottomClock(self):
        self.bottom.rotateClock()
        temp1 = self.front.face[6]
        temp2 = self.front.face[7]
        temp3 = self.front.face[8]
        self.front.face[6] = self.right.face[8]
        self.front.face[7] = self.right.face[5]
        self.front.face[8] = self.right.face[2]
        self.right.face[8] = self.back.face[2]
        self.right.face[5] = self.back.face[1]
        self.right.face[2] = self.back.face[0]
        self.back.face[2] = self.left.face[0]
        self.back.face[1] = self.left.face[3]
        self.back.face[0] = self.left.face[6]
        self.left.face[0] = temp1
        self.left.face[3] = temp2
        self.left.face[6] = temp3
    
    # Rotate the front clockwise
    def frontClock(self):
        self.front.rotateClock()
        temp1 = self.top.face[6]
        temp2 = self.top.face[7]
        temp3 = self.top.face[8]
        self.top.face[6] = self.left.face[6]
        self.top.face[7] = self.left.face[7]
        self.top.face[8] = self.left.face[8]
        self.left.face[6] = self.bottom.face[2]
        self.left.face[7] = self.bottom.face[1]
        self.left.face[8] = self.bottom.face[0]
        self.bottom.face[2] = self.right.face[6]
        self.bottom.face[1] = self.right.face[7]
        self.bottom.face[0] = self.right.face[8]
        self.right.face[6] = temp1
        self.right.face[7] = temp2
        self.right.face[8] = temp3

    # Rotate the front counterclockwise
    def frontCounter(self):
        self.front.rotateCounter()
        temp1 = self.top.face[6]
        temp2 = self.top.face[7]
        temp3 = self.top.face[8]
        self.top.face[6] = self.right.face[6]
        self.top.face[7] = self.right.face[7]
        self.top.face[8] = self.right.face[8]
        self.right.face[6] = self.bottom.face[2]
        self.right.face[7] = self.bottom.face[1]
        self.right.face[8] = self.bottom.face[0]
        self.bottom.face[2] = self.left.face[6] 
        self.bottom.face[1] = self.left.face[7]
        self.bottom.face[0] = self.left.face[8]
        self.left.face[6] = temp1
        self.left.face[7] = temp2
        self.left.face[8] = temp3
    
    # Rotate the back side clockwise.
    def backClock(self):
        self.back.rotateCounter()
        temp1 = self.top.face[0]
        temp2 = self.top.face[1]
        temp3 = self.top.face[2]
        self.top.face[0] = self.left.face[0]
        self.top.face[1] = self.left.face[1]
        self.top.face[2] = self.left.face[2]
        self.left.face[0] = self.bottom.face[6]
        self.left.face[1] = self.bottom.face[7]
        self.left.face[2] = self.bottom.face[8]
        self.bottom.face[6] = self.right.face[2]
        self.bottom.face[7] = self.right.face[1]
        self.bottom.face[8] = self.right.face[0]
        self.right.face[2] = temp3
        self.right.face[1] = temp2
        self.right.face[0] = temp1

    # Rotate the back side counter-clockwise.
    def backCounter(self):
        self.back.rotateClock()
        temp1 = self.top.face[0]
        temp2 = self.top.face[1]
        temp3 = self.top.face[2]
        self.top.face[0] = self.right.face[0]
        self.top.face[1] = self.right.face[1]
        self.top.face[2] = self.right.face[2]
        self.right.face[0] = self.bottom.face[8]
        self.right.face[1] = self.bottom.face[7]
        self.right.face[2] = self.bottom.face[6]
        self.bottom.face[8] = self.left.face[2]
        self.bottom.face[7] = self.left.face[1]
        self.bottom.face[6] = self.left.face[0]
        self.left.face[2] = temp3
        self.left.face[1] = temp2
        self.left.face[0] = temp1

# Main Application Class
class RubikCube:

    def solve(self):
        Cube = Rubik()
        f = open(sys.argv[1], "r")
        #Tried to refactor this but got a bunch of errors? Not sure whats going on.
        # Read in the files.
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
        # Create an initial open and closed list.
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


# On start.
if __name__=="__main__":    
    c = RubikCube()
    print c.solve()
