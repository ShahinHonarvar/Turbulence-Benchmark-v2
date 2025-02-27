def gcf_two_nums(lst):
    a, b = (lst[47], lst[75])
    while b:
        a, b = (b, a % b)
    return a