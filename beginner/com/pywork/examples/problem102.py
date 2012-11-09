import os
from com.pywork.examples.runutility import timing

def area(p1, p2, p3):
    return abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / float(2)

def contains_origin(p1, p2, p3):
    return area(p1, p2, (0,0)) + area(p1, p3, (0,0)) + area(p2, p3, (0,0)) == area(p1, p2, p3)

def read_points(filename):
    return [read_line(w) for w in (open(full_path(filename))).readlines()]

def read_line(line):
    list = line.rstrip().split(",")
    return map(int, list[0:2]), map(int, list[2:4]), map(int, list[4:6])

def full_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)

@timing
def answer(filename):
    return sum([1 if contains_origin(pointSet[0], pointSet[1], pointSet[2]) else 0 for pointSet in (read_points(filename))])

