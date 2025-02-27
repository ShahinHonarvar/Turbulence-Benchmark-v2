def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) < 77:
        return None
    first = lst[76]
    second = lst[35]
    third = lst[74]
    return gcd(gcd(first, second), third)