def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[69:71] if x % 72 == 0 or x % 70 == 0)) if len(lst) > 70 else 0