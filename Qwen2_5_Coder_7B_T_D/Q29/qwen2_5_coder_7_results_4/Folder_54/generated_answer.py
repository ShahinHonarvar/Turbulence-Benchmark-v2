def gcf_two_nums(lst):
    a, b = (lst[56], lst[92])
    while b:
        a, b = (b, a % b)
    return a