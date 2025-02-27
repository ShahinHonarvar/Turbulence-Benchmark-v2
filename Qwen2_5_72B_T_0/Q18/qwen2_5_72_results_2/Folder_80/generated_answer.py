def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[14:94], start=14) if x % 71 == 0 or x % 81 == 0))