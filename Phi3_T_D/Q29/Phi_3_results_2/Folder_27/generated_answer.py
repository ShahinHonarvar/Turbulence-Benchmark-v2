def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_15 = lst[15] if len(lst) > 15 else None
    index_40 = lst[40] if len(lst) > 40 else None
    if index_15 is None or index_40 is None:
        return None
    elif index_15 == 0 or index_40 == 0:
        return 1
    else:
        return gcd(index_15, index_40)