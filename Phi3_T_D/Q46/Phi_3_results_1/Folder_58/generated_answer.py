from math import gcd

def gcf_three_nums(lst):

    def gcf_two(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(lst[145], gcd(lst[183], lst[770]))