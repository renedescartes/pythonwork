import itertools
import runutility

def is_special_sum_set(inputs):
    inputs.sort()
    rule2_satisfied = is_rule2_satisfied(inputs)
    print "Inputs %s" % inputs
    return rule2_satisfied and is_rule1_satisfied(inputs)

def powerset(s):
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def is_rule1_satisfied(inputs):
    for r in range(1, len(inputs)):
        combination1 = itertools.combinations(inputs, r)
        for subset1 in combination1:
            combination2 = itertools.combinations(inputs, r)
            for subset2 in combination2:
                if (set(subset1) != set(subset2)) and (sum(subset1) == sum(subset2)):
                    return False
    return True

def is_rule2_satisfied(inputs):
    return runutility.find(lambda length: sum(inputs[-1 * length:]) >= sum(inputs[:length+1]), range(1, len(inputs))) is None

def read_elements(input_file):
    return [map(int, w.rstrip().split(",")) for w in (open(runutility.full_path(input_file))).readlines()]

def answer(input_file):
    return sum([1 if is_special_sum_set(input) else 0 for input in (read_elements(input_file))])