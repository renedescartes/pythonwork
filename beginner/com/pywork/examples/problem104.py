ALL_DIGIT_SET = set([str(i) for i in range(1, 10)])

def is_pandigital(n):
    digitSet = set(str(n))
    return len(str(n)) == 9 and len(digitSet) == 9 and len(digitSet - ALL_DIGIT_SET) == 0