def gcf_two_nums(lst):
    a = lst[84 % len(lst)]
    b = lst[21 % len(lst)]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(a, b)