def gcf_two_nums(lst):
    a = lst[95]
    b = lst[73]
    while b != 0:
        a, b = (b, a % b)
    return a