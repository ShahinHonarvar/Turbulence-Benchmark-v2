def if_perfect_num(lst):
    return sum((lst[33] // i for i in range(1, lst[33]))) == lst[33] - 1 if len(lst) > 33 else False