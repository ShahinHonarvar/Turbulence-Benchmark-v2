def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[25:71], start=25) if x % 74 == 0 or x % 15 == 0))