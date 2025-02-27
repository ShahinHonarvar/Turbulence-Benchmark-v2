def gcf_two_nums(lst):
    return gcd(lst[85], lst[33])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a