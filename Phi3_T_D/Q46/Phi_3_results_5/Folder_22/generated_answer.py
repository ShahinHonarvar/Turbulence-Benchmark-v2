import math

def gcf_three_nums(lst):
    if len(lst) < max(27, 85, 51):
        raise IndexError('Input list must have at least 85 elements.')
    x = lst[27]
    y = lst[85]
    z = lst[51]
    gcd_xy = math.gcd(x, y)
    return math.gcd(gcd_xy, z)