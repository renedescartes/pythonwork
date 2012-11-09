def subMatrix(matrix, rowNumber):
    """
    Given a matrix and a row number this method computes a sub matrix for the cofactor of the element in the first column
    of that given row number.
    """
    newMatrix = [row[1:] for row in matrix]
    del newMatrix[rowNumber]
    return newMatrix

def determinant(matrix):
    """
    Computes the determinant of a matrix. Please note responsibility of caller to call with a square matrix
    """
    return matrix[0][0] if len(matrix) == 1 else \
        sum([determinant(subMatrix(matrix, rowNumber)) * matrix[rowNumber][0] * pow(-1, rowNumber+1) for rowNumber in range(0, len(matrix))])

def evaluate(polynomial, n):
    """
    Given a polynomial as a list for example [6, -11, 6] means 6n^2 - 11n + 6
    This method evaluates the value of a polynomial for a given n
    """
    return sum([polynomial[termNumber] * pow(n, len(polynomial) - termNumber -1) for termNumber in range(0, len(polynomial))])

def evaluateTerms(polynomial, n):
    """
    Given a polynomial and N this method evaluates the first N terms
    """
    return [evaluate(polynomial, i) for i in range(1, n+1)]