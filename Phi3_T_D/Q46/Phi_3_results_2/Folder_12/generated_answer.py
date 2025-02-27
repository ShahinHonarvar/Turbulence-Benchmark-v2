def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) > 48:
        first = lst[91 % len(lst)]
        second = lst[45 % len(lst)]
        third = lst[48 % len(lst)]
        return gcd(gcd(first, second), third)
    else:
        raise ValueError('List must contain at least 92 elements')