def if_perfect_num(lst):
    return sum((x for x in range(1, lst[74]) if lst[74] % x == 0)) == lst[74]