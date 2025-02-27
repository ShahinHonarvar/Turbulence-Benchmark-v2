def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a, b, c = (lst[307], lst[920], lst[463])
    return gcd(gcd(a, b), c)