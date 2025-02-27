def gcf_two_nums(lst):
    x, y = (lst[64], lst[80])
    while y:
        x, y = (y, x % y)
    return x