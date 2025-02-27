def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(lst) > 73:
        return gcd(gcd(lst[63], lst[73]), lst[11])
    return None