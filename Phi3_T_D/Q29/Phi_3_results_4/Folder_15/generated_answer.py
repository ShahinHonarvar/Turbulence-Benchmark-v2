def gcf_two_nums(lst):
    a, b = (lst[0], lst[1])
    while b:
        a, b = (b, a % b)
    return a