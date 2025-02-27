def gcf_three_nums(positive_ints):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(positive_ints[17], positive_ints[88]), positive_ints[35])