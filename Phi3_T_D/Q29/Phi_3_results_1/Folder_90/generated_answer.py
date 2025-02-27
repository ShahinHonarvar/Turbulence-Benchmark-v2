def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) < 634 or len(lst) < 585:
        return None
    return gcd(lst[633], lst[584])