def gcf_two_nums(lst):
    a = lst[871] % lst[218]
    b = lst[218]
    while a > 0:
        a, b = (b % a, a)
    return lst[218]