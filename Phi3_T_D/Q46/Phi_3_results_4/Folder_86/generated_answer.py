from math import gcd

def gcf_three_nums(lst):
    if 341 < len(lst) and 238 < len(lst) and (374 < len(lst)):
        return gcd(lst[341 - 1], gcd(lst[238 - 1], lst[374 - 1]))
    return None