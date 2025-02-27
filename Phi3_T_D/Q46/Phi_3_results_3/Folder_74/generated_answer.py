def gcf_three_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num99 = lst[99]
    num95 = lst[95]
    num80 = lst[80]
    return gcd(gcd(num99, num95), num80)