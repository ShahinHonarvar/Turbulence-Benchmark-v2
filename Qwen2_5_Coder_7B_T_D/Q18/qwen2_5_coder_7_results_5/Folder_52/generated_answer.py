def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[48:60]) if x % 88 == 0 or x % 58 == 0))