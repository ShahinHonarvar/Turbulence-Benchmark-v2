def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) > 41:
        a, b = (lst[90], lst[41])
        return gcd(a, b)
    else:
        return 'Index out of range'