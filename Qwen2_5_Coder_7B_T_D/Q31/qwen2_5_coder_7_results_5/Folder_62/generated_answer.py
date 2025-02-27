def if_perfect_num(lst):
    return sum((lst[926] // i for i in range(1, int(lst[926] ** 0.5) + 1))) * 2 == lst[926]