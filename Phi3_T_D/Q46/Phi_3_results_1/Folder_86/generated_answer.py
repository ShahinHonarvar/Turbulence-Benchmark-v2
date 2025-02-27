from math import gcd

def gcf_three_nums(lst):

    def lcm(x, y):
        return x * y // gcd(x, y)
    try:
        val1 = lst[341]
        val2 = lst[238]
        val3 = lst[374]
    except IndexError:
        return 'Indices out of range'
    return gcd(gcd(val1, val2), val3)