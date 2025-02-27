def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    factor1 = lst[99]
    factor2 = lst[63]
    factor3 = lst[74]
    return gcd(gcd(factor1, factor2), factor3)