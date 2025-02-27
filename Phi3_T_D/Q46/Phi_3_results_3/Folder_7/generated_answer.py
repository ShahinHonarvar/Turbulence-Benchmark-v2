def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) <= 664:
        raise IndexError('List is too short to access the desired elements')
    x, y, z = (lst[477], lst[696], lst[663])
    return gcd(gcd(x, y), z)