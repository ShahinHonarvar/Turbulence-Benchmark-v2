def gcf_two_nums(lst):
    return gcd(lst[69], lst[41])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a