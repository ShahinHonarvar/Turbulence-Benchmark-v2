def gcf_three_nums(lst):
    a = lst[31]
    b = lst[25]
    c = lst[80]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)