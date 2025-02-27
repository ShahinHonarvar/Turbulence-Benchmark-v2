def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    x = lst[37] if len(lst) > 37 else None
    y = lst[30] if len(lst) > 30 else None
    return gcd(x, y) if x is not None and y is not None else None