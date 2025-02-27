def gcf_two_nums(lst):
    return gcd(lst[49], lst[53])

def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a