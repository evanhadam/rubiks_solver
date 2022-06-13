from cube import Cube
import align

def scanFaceWhiteEdges(cube, color):
        face = cube.assignFace(color)
        whiteEdgeLocation = []
        for row in range(3):
            for col in range(3):
                current = cube.cube[face][row][col]
                if current == 0 and (((row == 0 or row == 2) and col == 1) or (row == 1 and (col == 0 or col == 2))):
                    whiteEdgeLocation.append((row, col))
        return whiteEdgeLocation

# checks whole cube for white edges
def checkWhiteEdges(cube):
    for i in range(6):
        if not scanFaceWhiteEdges(cube, i) == []:
            return False
    return True

# takes a face and readjusts all edges on it
def orientWhiteEdge(cube, color):
    edges = scanFaceWhiteEdges(cube, color)
    position = cube.assignFace(color)
    if position == 1 or position == 2 or position == 3 or position == 4:
        for i in edges:
            if i == (0, 1):
                orientEdge01(cube, color)

def orientEdge01(cube, color):
    cube.shiftFaceToFront(color)
    if cube.checkForMatchesCenter(cube.cube[0][2][1], 1, 3):
        if cube.checkForMatchCenter(cube.cube[0][2][1], 1):
            cube.forwardPrime(color)
            cube.left(color)
            cube.forward(color)
        else:
            cube.forward(color)
            cube.right(color)
            cube.forwardPrime(color)
    # continue here for vase if corresponding piece == center color
    # elif cube.checkForMatchCenter(cube.cube[0][2][1], 2):