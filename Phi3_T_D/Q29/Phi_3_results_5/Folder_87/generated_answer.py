def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(lst) < 14:
        return None
    return gcd(lst[83], lst[14])