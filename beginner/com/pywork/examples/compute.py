def subMatrix(matrix, rowNumber):
    newMatrix = [row[1:] for row in matrix]
    del newMatrix[rowNumber]
    return newMatrix

def determinant(matrix):
    return matrix[0][0] if len(matrix) == 1 else \
        sum([determinant(subMatrix(matrix, rowNumber)) * matrix[rowNumber][0] * pow(-1, rowNumber+1) for rowNumber in range(0, len(matrix))])

def evaluate(polynomial, n):
    return sum([polynomial[termNumber] * pow(n, len(polynomial) - termNumber -1) for termNumber in range(0, len(polynomial))])

def evaluateTerms(polynomial, n):
    return [evaluate(polynomial, i) for i in range(1, n+1)]