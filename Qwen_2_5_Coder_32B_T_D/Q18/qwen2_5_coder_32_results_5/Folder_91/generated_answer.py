def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[:5] if x % 8 == 0 or x % -3 == 0)) if lst[:5] else 0