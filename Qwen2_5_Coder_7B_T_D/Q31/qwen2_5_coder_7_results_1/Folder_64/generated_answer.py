def if_perfect_num(lst):
    return sum((lst[1] // i for i in range(1, lst[1]))) == lst[1]