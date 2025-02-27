from math import gcd

def gcf_three_nums(lst):
    num1 = lst[8] if len(lst) >= 9 else None
    num2 = lst[2] if len(lst) >= 3 else None
    num3 = lst[1] if len(lst) >= 2 else None
    if num1 is None or num2 is None or num3 is None:
        return 'List is not long enough'
    return gcd(gcd(num1, num2), num3)