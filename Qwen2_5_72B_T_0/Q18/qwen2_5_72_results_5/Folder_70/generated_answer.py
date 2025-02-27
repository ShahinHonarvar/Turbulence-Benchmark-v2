def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[42:44] if x % 15 == 0 or x % 87 == 0)) if len(lst) > 43 else 0