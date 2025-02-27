def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[18:53], start=18) if x % 15 == 0 or x % 57 == 0))