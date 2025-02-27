def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(lst[894] if 894 < len(lst) else 0, lst[801] if 801 < len(lst) else 0)