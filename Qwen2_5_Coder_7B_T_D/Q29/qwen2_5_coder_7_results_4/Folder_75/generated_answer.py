def gcf_two_nums(lst):
    a = lst[42]
    b = lst[25]
    while b:
        a, b = (b, a % b)
    return a