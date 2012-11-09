import timeit
from com.pywork.examples.runutility import timing

def sub_matrix(matrix, rowNumber):
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
        sum([determinant(sub_matrix(matrix, rowNumber)) * matrix[rowNumber][0] * pow(-1, rowNumber+1) for rowNumber in range(0, len(matrix))])

def evaluate(polynomial, n):
    """
    Given a polynomial as a list for example [6, -11, 6] means 6n^2 - 11n + 6
    This method evaluates the value of a polynomial for a given n
    """
    return sum([polynomial[termNumber] * pow(n, len(polynomial) - termNumber -1) for termNumber in range(0, len(polynomial))])

def evaluate_terms(polynomial, n):
    """
    Given a polynomial and N this method evaluates the first N terms
    """
    return [evaluate(polynomial, i) for i in range(1, n+1)]

def vander_monde_matrix(n):
    """
    Returns a vander monde matrix with N terms http://en.wikipedia.org/wiki/Polynomial_interpolation
    (section - Constructing the interpolation polynomial)
    """
    return [[pow(row, n - column) for column in range(1, n+1)] for row in range(1, n+1)]

def cramers_solution(matrix, output):
    """
    Given a matrix and and output this method solves the problem using Cramers rule
    http://en.wikipedia.org/wiki/Cramer%27s_rule
    """
    d = determinant(matrix)
    return [determinant(replace_column(matrix, output, columnNumber))/d for columnNumber in range(0, len(matrix))]

def replace_column(matrix, column, columnNumber):
    """
    Replace a columnNumber in a matrix with the given column array
    """
    newMatrix = [row[:] for row in matrix]
    for rowIndex in range(0, len(newMatrix)):
        newMatrix[rowIndex][columnNumber] = column[rowIndex]
    return newMatrix

def first_incorrect_term(polynomial, terms):
    """
    Given a polynomial and a set of terms this method returns the First Incorrect Term
    as described in Problem101 of Euler
    """
    for index in range(len(polynomial), len(terms)):
        if evaluate(polynomial, index) != terms[index-1]:
            return evaluate(polynomial, index)

@timing
def sum_of_bop(polynomial):
    terms = evaluate_terms(polynomial, len(polynomial) + 2)
    return sum([first_incorrect_term(cramers_solution(vander_monde_matrix(index), terms[:index]), terms) for index in range(1, len(polynomial))])
