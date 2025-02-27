def gcf_two_nums(lst):
    a = lst[18]
    b = lst[37]
    while b != 0:
        a, b = (b, a % b)
    return a