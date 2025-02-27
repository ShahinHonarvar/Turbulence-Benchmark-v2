from math import gcd

def gcf_three_nums(lst):
    num1, num2, num3 = (lst[64] if len(lst) > 64 else None, lst[80] if len(lst) > 80 else None, lst[15] if len(lst) > 15 else None)
    if num1 is not None and num2 is not None and (num3 is not None):
        return gcd(gcd(num1, num2), num3)
    else:
        return 'List does not have enough elements or indices are out of range.'