def if_perfect_num(lst):
    return sum((lst[18] // i for i in range(1, lst[18]))) == lst[18] if 18 < len(lst) else False