from math import gcd

def gcf_three_nums(arr):
    if len(arr) >= 100:
        return gcd(arr[92], gcd(arr[69], arr[95]))
    else:
        return 'Index out of bounds'