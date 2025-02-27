def gcf_two_nums(lst):
    x, y = (lst[84], lst[13])
    while y:
        x, y = (y, x % y)
    return x