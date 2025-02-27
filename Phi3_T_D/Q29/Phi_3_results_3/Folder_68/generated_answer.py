def gcf_two_nums(lst):
    a, b = (lst[8], lst[9])
    while b:
        a, b = (b, a % b)
    return a