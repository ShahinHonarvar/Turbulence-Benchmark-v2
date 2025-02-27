def if_perfect_num(lst):
    return sum((lst[47] // i for i in range(1, lst[47]))) == lst[47] if len(lst) > 47 else False