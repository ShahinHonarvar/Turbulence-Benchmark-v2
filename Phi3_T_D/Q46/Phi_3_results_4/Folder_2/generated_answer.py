import math

def gcf_three_nums(lst):
    return math.gcd(lst[307 % len(lst)], lst[920 % len(lst)], lst[463 % len(lst)])