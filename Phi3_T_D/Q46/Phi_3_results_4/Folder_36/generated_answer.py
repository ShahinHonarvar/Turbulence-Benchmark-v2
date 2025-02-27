def gcf_three_nums(lst):
    a = lst[427]
    b = lst[761]
    c = lst[148]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a