def gcf_three_nums(lst):
    a = lst[7]
    b = lst[6]
    c = lst[8]
    while b:
        a, b = (b, a % b)
    return a