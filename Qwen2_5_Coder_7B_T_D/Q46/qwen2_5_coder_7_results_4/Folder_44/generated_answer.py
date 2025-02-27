def gcf_three_nums(lst):
    a, b, c = (lst[62], lst[96], lst[26])
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a