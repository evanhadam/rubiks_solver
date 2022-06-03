import numpy as np

class Cube:
    # 0 = White, 1 = Green, 2 = Red, 3 = Orange, 4 = Blue, 5 = Yellow
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

    # Array Order = [Top, Left, Mid, Right, Back, Bottom]
    # color coordinated cube in beginning to test movements

    def __init__(self):
        self.cube = np.array([[[5 for i in range(3)] for j in range(3)],
                            [[2 for i in range(3)] for j in range(3)],
                            [[1 for i in range(3)] for j in range(3)],
                            [[3 for i in range(3)] for j in range(3)],
                            [[4 for i in range(3)] for j in range(3)],
                            [[0 for i in range(3)] for j in range(3)]])

    def shuffle():
        