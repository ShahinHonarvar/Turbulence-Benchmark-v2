def gcf_two_nums(lst):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    if len(lst) < max(69, 40):
        raise ValueError('List must contain at least 69 elements.')
    return gcd(lst[69], lst[40])