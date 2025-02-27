from math import gcd

def gcf_three_nums(lst):
    first_numbers = lst[9] if len(lst) > 9 else 0
    second_numbers = lst[6] if len(lst) > 6 else 0
    third_numbers = lst[2] if len(lst) > 2 else 0
    return gcd(gcd(first_numbers, second_numbers), third_numbers)