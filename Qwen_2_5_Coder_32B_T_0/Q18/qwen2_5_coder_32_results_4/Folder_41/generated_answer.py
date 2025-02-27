def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:10]) if i <= 9 and (x % 6 == 0 or x % -3 == 0)))