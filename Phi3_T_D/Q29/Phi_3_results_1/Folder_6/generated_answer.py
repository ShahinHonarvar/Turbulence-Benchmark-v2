def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) > 80:
        return gcd(lst[25], lst[80])
    else:
        raise ValueError('List must contain at least 81 elements')