def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (lst[990], lst[243], lst[973])
    return gcd(gcd(a, b), c)