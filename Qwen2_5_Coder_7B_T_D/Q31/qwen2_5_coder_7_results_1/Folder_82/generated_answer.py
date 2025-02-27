def if_perfect_num(lst):
    return sum((lst[83] // i for i in range(1, int(lst[83] ** 0.5) + 1))) - lst[83] == 1