def gcf_three_nums(lst):
    a, b, c = (lst[1], lst[2], lst[7])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a