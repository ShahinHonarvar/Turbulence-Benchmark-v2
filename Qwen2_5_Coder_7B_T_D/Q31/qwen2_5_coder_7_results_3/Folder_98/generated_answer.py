def if_perfect_num(lst):
    return sum((lst[4] // i for i in range(1, lst[4]))) == lst[4] and lst[4] != 1