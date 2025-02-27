def gcf_two_nums(lst):
    a = lst[48]
    b = lst[76]
    while b:
        a, b = (b, a % b)
    return a