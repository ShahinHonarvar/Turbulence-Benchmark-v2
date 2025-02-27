def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    factor_4_0 = gcd(lst[4], lst[0])
    return gcd(factor_4_0, lst[8])