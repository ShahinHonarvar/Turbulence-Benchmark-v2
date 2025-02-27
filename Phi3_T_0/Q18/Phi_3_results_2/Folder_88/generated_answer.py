def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[3:10], start=3) if x % 6 == 0 or x % 1 == 0))