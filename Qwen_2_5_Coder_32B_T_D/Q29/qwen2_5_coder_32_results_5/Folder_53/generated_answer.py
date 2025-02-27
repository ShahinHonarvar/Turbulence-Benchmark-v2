def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(lst):
    return gcd(lst[28], lst[67])