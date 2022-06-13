#import numpy as np
#import align



class Cube:
    # Cube Layout
    #            -----------
    #           |           |
    #           |    Top    |
    #           |           |
    #-----------|-----------|-----------------------
    #|          |           |          |           |
    #|   Left   |    Mid    |   Right  |    Back   |
    #|          |           |          |           |
    #-----------------------------------------------
    #           |           |
    #           |   Bottom  | 
    #           |           |
    #           -------------

    # Piece color: 0 = White, 1 = Green, 2 = Red, 3 = Orange, 4 = Blue, 5 = Yellow
    # Face orientation: Top is 0, Left is 1, Front is 2, Right is 3, Back is 4, Bottom is 5
    # Array Order = [Top, Left, Mid, Right, Back, Bottom]

    def __init__(self):
        white = [[4, 4, 5], [3, 0, 2], [5, 3, 5]]
        blue =  [[0, 0, 2], [4, 4, 5], [3, 3, 0]]
        orange = [[1, 5, 1], [2, 3, 2], [1, 4, 4]]
        green = [[3, 0, 4], [4, 1, 1], [2, 5, 0]]
        red = [[2, 5, 3], [2, 2, 0], [2, 0, 4]]
        yellow = [[3, 3, 0], [1, 5, 1], [5, 1, 1]]
        self.cube = [white,
                            blue,
                            orange,
                            green,
                            red,
                            yellow]
        self.SolveSteps = []

    def assignFace(self, faceColor):
        for i in range(6):
            if self.cube[i][1][1] == faceColor:
                return i

    # Parameters: i, j, k, l are all face center positions. Top is 0, Left is 1, Front is 2, Right is 3, Back is 4, Bottom is 5
    # shifts positions of faces on the cube. No changes are made except to orientation the cube is viewed from.
    def rotate(self, i, j, k, l):
        temp = self.cube[j]
        temp2 = self.cube[k]
        temp3 = self.cube[l]
        self.cube[j] = self.cube[i]
        self.cube[k] = temp
        self.cube[l] = temp2
        self.cube[i] = temp3

    # shifts the face(not pieces attached) 180 degrees clockwise
    def shiftSide180(self, sidePosition):
        for i in range(2):
                self.shiftSideCounterClock(sidePosition)

    # shifts the face(not pieces attached) 90 degrees clockwise
    def shiftSideClock(self, sidePosition):
        temp = self.cube[sidePosition][0][2]
        temp2 = self.cube[sidePosition][1][2]
        temp21 = self.cube[sidePosition][2][2]
        temp22 = self.cube[sidePosition][2][1]
        self.cube[sidePosition][0][2], self.cube[sidePosition][1][2] = self.cube[sidePosition][0][0], self.cube[sidePosition][0][1]
        self.cube[sidePosition][2][2], self.cube[sidePosition][2][1] = temp, temp2
        temp, temp2 = self.cube[sidePosition][1][0], self.cube[sidePosition][2][0]
        self.cube[sidePosition][1][0], self.cube[sidePosition][2][0] = temp22, temp21
        self.cube[sidePosition][0][0], self.cube[sidePosition][0][1] = temp2, temp

    # shifts the face(not pieces attached) 90 degrees counterclockwise
    def shiftSideCounterClock(self, sidePosition):
        for i in range(3):
            self.shiftSideClock(sidePosition)

    # orients the face with the center of a color of choice to the front of the cube
    def shiftFaceToFront(self, color):
        place = self.assignFace(color)
        if place == 0:
            self.rotate(0, 2, 5, 4)
            self.shiftSideClock(1)
            self.shiftSideCounterClock(3)
            self.shiftSide180(0)
            self.shiftSide180(4)
        elif place == 1:
            self.rotate(1, 2, 3, 4)
            self.shiftSideCounterClock(0)
            self.shiftSideClock(5)
        elif place == 3:
            for i in range(3):
                self.rotate(1, 2, 3, 4)
                self.shiftSideCounterClock(0)
                self.shiftSideClock(5)
        elif place == 4:
            for i in range(2):
                self.rotate(1, 2, 3, 4)
                self.shiftSideClock(0)
                self.shiftSideCounterClock(5)
        elif place == 5:
            for i in range(3):
                self.rotate(0, 2, 5, 4)
            self.shiftSide180(4)
            self.shiftSide180(5)
            self.shiftSideCounterClock(1)
            self.shiftSideClock(3)

    # twists a face + pieces attaached 90 degrees clockwise
    def turnSideClock(self, color):
        self.shiftFaceToFront(color)
        self.shiftSideClock(2)
        temp, temp2, temp3 = self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2]
        temp21, temp22, temp23 = self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0]
        self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2] = self.cube[1][2][2], self.cube[1][1][2], self.cube[1][0][2] 
        self.cube[3][0][0], self.cube[3][1][0], self.cube[3][2][0] = temp, temp2, temp3
        temp, temp2, temp3 = self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2]
        self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2] = temp23, temp22, temp21
        self.cube[1][0][2], self.cube[1][1][2], self.cube[1][2][2] = temp, temp2, temp3

    # twists a face + pieces attaached 90 degrees counterclockwise
    def turnSideCounterClock(self, color):
        for i in range(3):
            self.turnSideClock(color)

    # F
    def forward(self, color):
        self.turnSideClock(color)

    # F'
    def forwardPrime(self, color):
        for i in range(3):
            self.turnSideClock(color)

    # L
    def left(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[1][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[3][1][1])

    # L'
    def leftPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[1][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[3][1][1])

    # R
    def right(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[3][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[1][1][1])

    # R'
    def rightPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[3][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[1][1][1])

    # U
    def up(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[0][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[5][1][1])

    # U'
    def upPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[0][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[5][1][1])

    # D
    def down(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[5][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[0][1][1])

    # D'
    def downPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[5][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[0][1][1])

    def checkCenterColor(self, i):
        return self.cube[i][1][1]

    def checkForMatchCenter(self, original, centerPosition):
        return True if original == self.cube[centerPosition][1][1] else False
        
    def checkForMatchesCenter(self, original, centerPosition1, centerPosition2):
        if original == self.cube[centerPosition1][1][1] or original == self.cube[centerPosition2][1][1]:
            return True
        return False