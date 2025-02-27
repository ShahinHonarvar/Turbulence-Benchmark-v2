def gcf_three_nums(lst):
    a, b, c = (lst[63], lst[73], lst[11])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a