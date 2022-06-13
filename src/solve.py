from cube import Cube
import cross

test = Cube()

print(test.cube)
cross.orientWhiteEdge(test, 4)
test.shiftFaceToFront(3)
print(test.cube)