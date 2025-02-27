def if_perfect_num(lst):
    return sum((lst[51] // i for i in range(1, lst[51]))) == lst[51]