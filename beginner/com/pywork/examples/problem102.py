def area(p1, p2, p3):
    return abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))

def contains_origin(p1, p2, p3):
    origin = (0,0)
    return area(p1, p2, origin) + area(p1, p3, origin) + area(p2, p3, origin) == area(p1, p2, p3)