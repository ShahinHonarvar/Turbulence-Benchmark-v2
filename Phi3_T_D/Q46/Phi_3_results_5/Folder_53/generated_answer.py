def gcf_three_nums(lst):
    a, b, c = (lst[66], lst[56], lst[92])

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)