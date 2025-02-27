def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i < 10 and (x % 10 == 0 or x % 100 == 0)))