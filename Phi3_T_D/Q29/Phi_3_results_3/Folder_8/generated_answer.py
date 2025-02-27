def gcf_two_nums(lst):
    a = lst[69]
    b = lst[41]
    while b != 0:
        a, b = (b, a % b)
    return a