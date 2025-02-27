def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    idx_18, idx_10, idx_76 = (lst[18], lst[10], lst[76])
    return gcd(gcd(idx_18, idx_10), idx_76)