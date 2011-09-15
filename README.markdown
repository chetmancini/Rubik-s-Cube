# Rubik's Cube
_Project for Artificial Intelligence, CS4700, Cornell University_

## Representation

O = Orange
Y = Yellow
G = Green
B = Blue
W = White
R = Red

## Input

arg1: A text file in the following format:

          W W W
          W W W
          W W W
    G G G R R R B B B
    G G G R R R B B B
    G G G R R R B B B
          Y Y Y
          Y Y Y
          Y Y Y
          O O O
          O O O
          O O O

    #Back
    W W W
    W W W
    W W W
    #Left
    G G G
    G G G
    G G G
    #Top
    R R R 
    R R R 
    R R R
    #Right 
    B B B
    B B B
    B B B
    #Front
    Y Y Y
    Y Y Y
    Y Y Y
    #Bottom
    O O O
    O O O
    O O O


### Explanation ###
The center square is the "top" of the cube.
The square directly below it is the front.

## Output

\# of moves


