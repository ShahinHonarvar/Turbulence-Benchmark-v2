def gcf_three_nums(lst):
    a = lst[8]
    b = lst[2]
    c = lst[1]

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcd(gcd(a, b), c)