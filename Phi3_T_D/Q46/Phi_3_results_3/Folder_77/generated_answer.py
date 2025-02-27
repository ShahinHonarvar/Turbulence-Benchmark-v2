def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    first = gcd(lst[693], lst[331])
    return gcd(first, lst[668])