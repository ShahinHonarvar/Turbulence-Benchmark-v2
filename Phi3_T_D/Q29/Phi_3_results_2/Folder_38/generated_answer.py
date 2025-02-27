def gcf_two_nums(ints):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(ints[88], ints[35])