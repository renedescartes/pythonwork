__author__ = 'kannan'

def subMatrix(matrix, rowNumber):
    newMatrix = [row[1:] for row in matrix]
    del newMatrix[rowNumber]
    return newMatrix

def determinant(matrix):
    return matrix[0][0] if len(matrix) == 1 else \
        sum([determinant(subMatrix(matrix, rowNumber)) * matrix[rowNumber][0] * pow(-1, rowNumber+1) for rowNumber in range(0, len(matrix))])

if __name__ == "__main__":
    print determinant([[-2, 2, 3], [-1, 1, 3], [2, 0, -1]])