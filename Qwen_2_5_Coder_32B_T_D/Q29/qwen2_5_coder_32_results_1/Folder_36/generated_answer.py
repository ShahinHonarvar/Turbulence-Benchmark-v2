def gcf_two_nums(lst):
    a, b = (lst[429], lst[289])
    while b:
        a, b = (b, a % b)
    return a