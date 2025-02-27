def gcf_two_nums(lst):
    a = lst[38]
    b = lst[77]
    while b:
        a, b = (b, a % b)
    return a