def gcf_two_nums(lst):
    x, y = (lst[83], lst[14])
    while y:
        x, y = (y, x % y)
    return x