import math

def gcf_three_nums(lst):
    index25 = lst[25]
    index76 = lst[76]
    index57 = lst[57]
    return math.gcd(index25, math.gcd(index76, index57))