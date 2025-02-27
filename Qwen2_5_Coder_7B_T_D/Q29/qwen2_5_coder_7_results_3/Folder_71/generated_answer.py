def gcf_two_nums(lst):
    a = lst[78]
    b = lst[93]
    while b:
        a, b = (b, a % b)
    return a