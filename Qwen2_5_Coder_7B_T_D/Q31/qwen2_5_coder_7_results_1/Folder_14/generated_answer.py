def if_perfect_num(lst):
    return sum((lst[17] // i for i in range(1, lst[17]))) == lst[17] and lst[17] != 1