def gcf_two_nums(lst):
    x = lst[51]
    y = lst[31]
    while y:
        x, y = (y, x % y)
    return x