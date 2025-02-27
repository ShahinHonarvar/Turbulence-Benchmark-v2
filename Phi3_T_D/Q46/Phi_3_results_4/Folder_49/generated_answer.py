def gcf_three_nums(lst):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(lst) < 78:
        return None
    num34 = lst[34]
    num38 = lst[38]
    num77 = lst[77]
    return gcd(gcd(num34, num38), num77)