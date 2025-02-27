def gcf_two_nums(lst):

    def gcd(a, b):
        return a if not b else gcd(b, a % b)
    return gcd(lst[87], lst[34])