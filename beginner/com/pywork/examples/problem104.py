ALL_DIGIT_SET = set([i for i in range(1, 10)])

def is_pandigital(n):
    digitList = map(int, n) if isinstance(n, list) else map(int, str(n))
    digitSet = set(digitList)
    return len(digitList) == 9 and len(digitSet) == 9 and len(digitSet - ALL_DIGIT_SET) == 0

def answer():
    k, a, b = 2, [1], [1]
    while True:
        ends_with_pandigital = is_pandigital(b[-9:])
        starts_with_pandigital = is_pandigital(b[:9])
        if ends_with_pandigital or starts_with_pandigital:
            print "k = %s start = %s end = %s" % (k, starts_with_pandigital, ends_with_pandigital)
        if starts_with_pandigital and ends_with_pandigital:
            return k
        k, a, b = k + 1, b, add_big_number(a, b)

def add_big_number(list1, list2):
    answer, rlist1, rlist2 = [], list1[::-1], list2[::-1]
    carry = 0
    for d in range(0, max(len(list1), len(list2))):
        total = carry + (rlist1[d] if d < len(rlist1) else 0) + (rlist2[d] if d < len(rlist2) else 0)
        answer.append(total % 10)
        carry = total/10
    if carry > 0:
        answer.append(carry)
    return answer[::-1]