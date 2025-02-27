def gcf_three_nums(positive_integers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(positive_integers[15], gcd(positive_integers[51], positive_integers[76]))