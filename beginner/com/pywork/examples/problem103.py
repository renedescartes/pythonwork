import itertools
import runutility

def is_special_sum_set(inputs):
    return is_rule1_satisfied(inputs) & is_rule2_satisfied(inputs)

def powerset(iterable):
    s = list(iterable)
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
        current = map(lambda i: i + b, current)
        current.insert(0, b)
    return current


