def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[41:57]) if x % 82 == 0 or x % 90 == 0))