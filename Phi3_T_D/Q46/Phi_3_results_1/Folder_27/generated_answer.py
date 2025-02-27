def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_three(lst[76], lst[64], lst[28])