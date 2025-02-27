def gcf_two_nums(lst):
    return gcd(lst[84], lst[13])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a