def gcf_two_nums(lst):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    index_60 = 60
    index_64 = 64
    if index_60 < len(lst) and index_64 < len(lst):
        return gcd(lst[index_60], lst[index_64])
    else:
        return None