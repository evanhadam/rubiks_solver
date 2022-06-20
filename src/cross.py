from cube import Cube
import align

# scans a face for white edges, and returns a list of tuples that give the rows and columns of the edges in (row, col) format
def scanFaceWhiteEdges(cube, color):
        face = cube.assignFace(color)
        whiteEdgeLocation = []
        for row in range(3):
            for col in range(3):
                current = cube.cube[face][row][col]
                if current == 0 and (((row == 0 or row == 2) and col == 1) or (row == 1 and (col == 0 or col == 2))):
                    whiteEdgeLocation.append((row, col))
        return whiteEdgeLocation

# takes a face and readjusts all edges on it
def orientWhiteEdge(cube, color):
    edges = scanFaceWhiteEdges(cube, color)
    position = cube.assignFace(color)

    for i in edges:
        if i == (0, 1):
            orientEdge01(cube, color)
            edges = scanFaceWhiteEdges(cube, color)
            continue
        elif i == (1, 0):
            orientEdge10(cube, color)
            edges = scanFaceWhiteEdges(cube, color)
            continue
        elif i == (1, 2):
            orientEdge12(cube, color)
            edges = scanFaceWhiteEdges(cube, color)
            continue
        elif i == (2, 1):
            orientEdge21(cube, color)
            edges = scanFaceWhiteEdges(cube, color)
            continue

# orients the top middle edge of a face onto the face with the yellow center
def orientEdge01(cube, color):
    cube.shiftFaceToFront(color)
    
    if color != 0:
        if cube.cube[5][1][2] != 0:
            cube.forward(color)
            cube.rightPrime(color)
            cube.forwardPrime(color)

        elif cube.cube[5][1][0] != 0:
            cube.forwardPrime(color)
            cube.left(color)
            cube.forward(color)

        elif cube.cube[5][0][1] != 0:
            cube.downPrime(color)
            cube.left(color)
            cube.down(color)

        else:
            cube.down(color)
            cube.left(color)
            cube.downPrime(color)

    else:
        while cube.cube[4][1][2] == 0:
            cube.forward(color)
            cube.rotate0153()
        cube.up2(color)

# orients the middle left edge of a face onto the face with the yellow center
def orientEdge10(cube, color):
    cube.shiftFaceToFront(color)

    if color != 0:
        if cube.cube[5][1][0] != 0:
            cube.left(color)

        elif cube.cube[5][0][1] != 0:
            cube.downPrime(color)
            cube.left(color)
            cube.down(color)

        elif cube.cube[5][1][2] != 0:
            cube.down2(color)
            cube.left(color)
            cube.down2(color)

        else:
            cube.down(color)
            cube.left(color)
            cube.downPrime(color)
            
    else:
        while cube.cube[4][1][2] == 0:
            cube.forward(color)
            cube.rotate0153()
        cube.left2(color)

# orients the middle right edge of a face onto the face with the yellow center
def orientEdge12(cube, color):
    cube.shiftFaceToFront(color)

    if color != 0:
        if cube.cube[5][1][2] != 0:
            cube.rightPrime(color)

        elif cube.cube[5][0][1] != 0:
            cube.down(color)
            cube.rightPrime(color)
            cube.downPrime(color)

        elif cube.cube[5][1][0] != 0:
            cube.down2(color)
            cube.rightPrime(color)
            cube.down2(color)

        else:
            cube.downPrime(color)
            cube.rightPrime(color)
            cube.down(color)
            
    else:
        while cube.cube[4][1][0] == 0:
            cube.forward(color)
            cube.rotate0153()
        cube.right2(color)

# orients the bottom middle edge of a face onto the face with the yellow center
def orientEdge21(cube, color):
    cube.shiftFaceToFront(color)


    if color != 0:
        cube.forward(color)
        cube.downPrime(color)
        cube.left(color)
        cube.forwardPrime(color)
        cube.down(color)
            
    else:
        while cube.cube[4][2][1] == 0:
            cube.forward(color)
            cube.rotate0153()
        cube.down2(color)

# orients all of the white edges on the cube onto the yellow face
def orientWhiteToYellow(cube):
    for i in range(2):
        for j in range(5):
            orientWhiteEdge(cube, j)

# orients all of the white edges on the yellow face back onto the white face with the proper orientation
# proper orientation: where the opposite edge attached to the white edge matches with its respective center color
def orientYellowToWhite(cube):
    cube.shiftFaceToFront(5)
    printWhiteEdges(cube)

    while cube.cube[2][0][1] == 0 or cube.cube[2][1][0] == 0 or cube.cube[2][1][2] == 0 or cube.cube[2][2][1] == 0:
        if cube.cube[0][2][1] == cube.cube[0][1][1]:
            cube.up2(5)
            cube.rotate0153()
        elif cube.cube[1][1][2] == cube.cube[1][1][1]:
            cube.left2(5)
            cube.rotate0153()
        elif cube.cube[3][1][0] == cube.cube[3][1][1]:
            cube.right2(5)
            cube.rotate0153()
        elif cube.cube[5][0][1] == cube.cube[5][1][1]:
            cube.forward2(5)
            cube.rotate0153()

        cube.forward(5)

    cube.shiftFaceToFront(3)
    cube.shiftWhiteToTop()

# prints edge colors on same piece as each white edge for testing purposes
def printWhiteEdges(cube):
    count = []
    edges = [cube.cube[0][0][1], cube.cube[4][0][1], cube.cube[0][1][0], cube.cube[1][0][1], cube.cube[0][2][1], cube.cube[2][0][1], cube.cube[0][1][2], cube.cube[3][0][1], cube.cube[1][1][0], cube.cube[4][1][2], cube.cube[1][1][2], cube.cube[2][1][0], cube.cube[1][2][1], cube.cube[5][1][0], cube.cube[2][2][1], cube.cube[5][0][1], cube.cube[2][1][2], cube.cube[3][1][0], cube.cube[3][2][1], cube.cube[5][1][2], cube.cube[3][1][2], cube.cube[4][1][0], cube.cube[4][2][1], cube.cube[5][2][1]]

    for i, color in enumerate(edges):
        
        if color == 0:
            if i % 2 == 0:
                count.append(edges[i + 1])
            else:
                count.append(edges[i - 1])
    
    print(count)

# main method that executes our entire cross algorithm in one line
def cross(cube):
    orientWhiteToYellow(cube)
    orientYellowToWhite(cube)