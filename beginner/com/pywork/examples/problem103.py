import itertools

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
    return False

