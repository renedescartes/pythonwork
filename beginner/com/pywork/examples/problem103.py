import itertools
import runutility

def is_special_sum_set(inputs):
    return is_rule1_satisfied(inputs) & is_rule2_satisfied(inputs)

def powerset(s):
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def is_rule1_satisfied(inputs):
    for subset1 in powerset(inputs):
        for subset2 in powerset(inputs):
            if (set(subset1) != set(subset2)) & (sum(subset1) == sum(subset2)):
                return False
    return True

def is_rule2_satisfied(inputs):
    return runutility.find(lambda length: sum(inputs[-1 * length:]) >= sum(inputs[:length+1]), range(1, len(inputs))) is None

def computed_optimal_set(n):
    current = [1]
    for index in range(1, n):
        b = current[len(current)/2]
        current = [b] + map(lambda i: i + b, current)
    return current

def adjustment_vector_iterator(n, adjustment):
    current = int("".join(map(str, [1 for i in range(n)])))
    high = int("".join(map(str, [n for i in range(n)])))
    while current <= high:
        if runutility.find(lambda digit: int(digit) > (2 * adjustment + 1) or int(digit) < 1, str(current)):
            yield map(lambda n : int(n) - adjustment - 1, str(current))
        current += 1

def is_valid_number(number, adjustment):
    for digit in str(number):
        if int(digit) > (2 * adjustment + 1) or int(digit) < 1:
            return False
    return True