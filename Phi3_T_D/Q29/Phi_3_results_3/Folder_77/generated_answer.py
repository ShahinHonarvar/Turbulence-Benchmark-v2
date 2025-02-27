def gcf_two_nums(lst):
    a = lst[840]
    b = lst[803]
    while b:
        a, b = (b, a % b)
    return a