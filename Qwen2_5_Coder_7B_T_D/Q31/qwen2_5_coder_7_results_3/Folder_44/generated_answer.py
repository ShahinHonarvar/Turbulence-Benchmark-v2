def if_perfect_num(lst):
    return sum([x for x in range(1, lst[828]) if lst[828] % x == 0]) == lst[828]