def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:11]) if i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and (x % 10 == 0 or x % 100 == 0)))