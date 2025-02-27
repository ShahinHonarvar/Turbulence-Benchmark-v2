def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    x, y, z = (lst[693], lst[331], lst[668])
    return gcd(gcd(x, y), z)