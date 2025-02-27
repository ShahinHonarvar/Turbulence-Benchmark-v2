def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    ind1, ind2, ind3 = (96, 53, 35)
    return gcd(lst[ind1], gcd(lst[ind2], lst[ind3]))