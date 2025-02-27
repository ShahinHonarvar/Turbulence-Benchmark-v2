def gcf_three_nums(lst):
    n1 = lst[19]
    n2 = lst[69]
    n3 = lst[97]
    gcf = gcd(gcd(n1, n2), n3)
    return gcf