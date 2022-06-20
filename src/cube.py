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
        white = [[0, 3, 0], [3, 0, 2], [4, 2, 3]]
        blue =  [[3, 0, 0], [5, 4, 5], [3, 0, 5]]
        orange = [[2, 1, 4], [2, 3, 3], [3, 4, 5]]
        green = [[5, 4, 1], [5, 1, 5], [2, 0, 5]]
        red = [[2, 1, 4], [1, 2, 4], [1, 3, 1]]
        yellow = [[1, 0, 4], [2, 5, 1], [0, 4, 1]]
        self.cube = [white,
                     blue,
                     orange,
                     green,
                     red,
                     yellow]
        self.solveSteps = []

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

    def rotate0153(self):
        self.rotate(0, 1, 5, 3)
        self.shiftSideCounterClock(0)
        self.shiftSideCounterClock(1)
        self.shiftSideCounterClock(2)
        self.shiftSideCounterClock(3)
        self.shiftSideClock(4)
        self.shiftSideCounterClock(5)
        
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

        if self.cube[5][1][1] == 0:
            for i in range(2):
                self.rotate0153()

    # shifts the cube back into it's default orientation when white isn't on the top or bottom(centers are in this order: white, blue, orange, green, red, yellow)
    def shiftWhiteToTop(self):
        if self.cube[1][1][1] == 0:
            for i in range(3):
                self.rotate0153()
        elif self.cube[2][1][1] == 0:
            for i in range(3):
                self.rotate(0, 2, 5, 4)
                self.shiftSideClock(1)
                self.shiftSideCounterClock(3)
                self.shiftSide180(0)
                self.shiftSide180(4)
        elif self.cube[3][1][1] == 0:
            self.rotate0153(self.cube[2][1][1])
        elif self.cube[4][1][1] == 0:
            self.rotate(0, 2, 5, 4)
            self.shiftSideClock(1)
            self.shiftSideCounterClock(3)
            self.shiftSide180(0)
            self.shiftSide180(4)
            

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

    # twists a side 180 degrees
    def turnSide180(self, color):
        self.turnSideClock(color)
        self.turnSideClock(color)

    # F
    def forward(self, color):
        self.turnSideClock(color)
        self.solveSteps.append("F " + self.convertNumToColor(color))

    # F'
    def forwardPrime(self, color):
        for i in range(3):
            self.turnSideClock(color)
        self.solveSteps.append("F' " + self.convertNumToColor(color))

    # F2
    def forward2(self, color):
        self.turnSide180(color)
        self.solveSteps.append("F2 " + self.convertNumToColor(color))

    # L
    def left(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[1][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[3][1][1])
        self.solveSteps.append("L " + self.convertNumToColor(color))

    # L'
    def leftPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[1][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[3][1][1])
        self.solveSteps.append("L' " + self.convertNumToColor(color))

    # L2
    def left2(self, color):
        for i in range(2):
            self.shiftFaceToFront(color)
            turnColor = self.cube[1][1][1]
            self.turnSideClock(turnColor)
            self.shiftFaceToFront(self.cube[3][1][1])
        self.solveSteps.append("L2 " + self.convertNumToColor(color))

    # R
    def right(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[3][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[1][1][1])
        self.solveSteps.append("R " + self.convertNumToColor(color))

    # R'
    def rightPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[3][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[1][1][1])
        self.solveSteps.append("R' " + self.convertNumToColor(color))

    # R2
    def right2(self, color):
        for i in range(2):
            self.shiftFaceToFront(color)
            turnColor = self.cube[3][1][1]
            self.turnSideClock(turnColor)
            self.shiftFaceToFront(self.cube[1][1][1])
        self.solveSteps.append("R2 " + self.convertNumToColor(color))
    # U
    def up(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[0][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[5][1][1])
        self.solveSteps.append("U " + self.convertNumToColor(color))

    # U'
    def upPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[0][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[5][1][1])
        self.solveSteps.append("U' " + self.convertNumToColor(color))

    # U2
    def up2(self, color):
        for i in range(2):
            self.shiftFaceToFront(color)
            turnColor = self.cube[0][1][1]
            self.turnSideClock(turnColor)
            self.shiftFaceToFront(self.cube[5][1][1])
        self.solveSteps.append("U2 " + self.convertNumToColor(color))

    # D
    def down(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[5][1][1]
        self.turnSideClock(turnColor)
        self.shiftFaceToFront(self.cube[0][1][1])
        self.solveSteps.append("D " + self.convertNumToColor(color))

    # D'
    def downPrime(self, color):
        self.shiftFaceToFront(color)
        turnColor = self.cube[5][1][1]
        self.turnSideCounterClock(turnColor)
        self.shiftFaceToFront(self.cube[0][1][1])
        self.solveSteps.append("D' " + self.convertNumToColor(color))

    def down2(self, color):
        for i in range(2):
            self.shiftFaceToFront(color)
            turnColor = self.cube[5][1][1]
            self.turnSideClock(turnColor)
            self.shiftFaceToFront(self.cube[0][1][1])
        self.solveSteps.append("D2 " + self.convertNumToColor(color))

    def checkCenterColor(self, i):
        return self.cube[i][1][1]

    def checkForMatchCenter(self, original, centerPosition):
        return True if original == self.cube[centerPosition][1][1] else False
        
    def checkForMatchesCenter(self, original, centerPosition1, centerPosition2):
        if original == self.cube[centerPosition1][1][1] or original == self.cube[centerPosition2][1][1]:
            return True
        return False

    # converts color number to color name
    def convertNumToColor(self, colorNum):
        colorName = ["white", "green", "red", "orange", "blue", "yellow"]

        return str(colorName[colorNum])