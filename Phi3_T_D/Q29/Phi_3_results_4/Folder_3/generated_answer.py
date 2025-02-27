def gcf_two_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(lst[47], lst[10]) if len(lst) > 47 and len(lst) > 10 else None