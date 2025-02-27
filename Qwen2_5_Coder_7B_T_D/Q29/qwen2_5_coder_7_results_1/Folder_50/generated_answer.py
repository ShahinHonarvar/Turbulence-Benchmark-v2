def gcf_two_nums(lst):
    a = lst[90]
    b = lst[54]
    while b:
        a, b = (b, a % b)
    return a