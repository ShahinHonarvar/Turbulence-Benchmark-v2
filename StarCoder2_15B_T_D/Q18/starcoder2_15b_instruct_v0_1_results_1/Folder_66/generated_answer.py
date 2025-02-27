def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i >= 58 and i <= 81 and (x % 55 == 0) or x % 10 == 0))