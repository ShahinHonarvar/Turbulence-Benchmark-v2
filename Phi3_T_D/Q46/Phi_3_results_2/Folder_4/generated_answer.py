def gcf_three_nums(values):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(values[24], values[25]), values[80])