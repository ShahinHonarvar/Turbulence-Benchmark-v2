def if_perfect_num(lst):
    return sum((x for x in range(1, lst[15]) if lst[15] % x == 0)) == lst[15] and lst[15] != 1