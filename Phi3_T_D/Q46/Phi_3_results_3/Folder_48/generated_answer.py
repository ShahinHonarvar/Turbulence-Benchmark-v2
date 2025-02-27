import math

def gcf_three_nums(arr):
    if len(arr) < max(654, 312, 441):
        return None
    return math.gcd(arr[654], arr[312], arr[441])