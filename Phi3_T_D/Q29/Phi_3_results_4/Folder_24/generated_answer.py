def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(lst[84] if 84 < len(lst) else 1, lst[21] if 21 < len(lst) else 1)