def gcf_three_nums(lst):

    def gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    return gcd(gcd(lst[4], lst[1]), lst[7])