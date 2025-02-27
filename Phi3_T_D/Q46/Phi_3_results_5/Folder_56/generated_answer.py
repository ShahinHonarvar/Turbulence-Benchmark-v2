import math

def gcf_three_nums(lst):
    if len(lst) > max(59, 93, 84):
        return math.gcd(math.gcd(lst[59], lst[93]), lst[84])
    else:
        raise IndexError('Index out of lists range.')