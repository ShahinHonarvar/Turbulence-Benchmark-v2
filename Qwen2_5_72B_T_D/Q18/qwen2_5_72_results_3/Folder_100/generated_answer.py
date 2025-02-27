def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[72:94], start=72) if x % 32 == 0 or x % 44 == 0))