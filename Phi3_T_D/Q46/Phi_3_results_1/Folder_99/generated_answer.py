from math import gcd

def gcf_three_nums(lst):

    def lcm(a, b):
        return a * b // gcd(a, b)
    index_912 = lst[912] if len(lst) > 912 else 1
    index_170 = lst[170] if len(lst) > 170 else 1
    index_500 = lst[500] if len(lst) > 500 else 1
    result = gcd(index_912, gcd(index_170, index_500))
    return result