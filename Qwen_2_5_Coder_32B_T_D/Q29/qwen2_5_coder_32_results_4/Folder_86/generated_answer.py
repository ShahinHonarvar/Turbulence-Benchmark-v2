def gcf_two_nums(lst):
    a, b = (lst[793], lst[449])
    while b:
        a, b = (b, a % b)
    return a