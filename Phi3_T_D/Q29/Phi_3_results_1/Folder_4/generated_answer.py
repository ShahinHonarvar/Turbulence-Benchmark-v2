def gcf_two_nums(lst):
    a = lst[75]
    b = lst[56]
    while b:
        a, b = (b, a % b)
    return a