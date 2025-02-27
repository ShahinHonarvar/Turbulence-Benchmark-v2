def gcf_two_nums(lst):

    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    return gcd(lst[534], lst[630])