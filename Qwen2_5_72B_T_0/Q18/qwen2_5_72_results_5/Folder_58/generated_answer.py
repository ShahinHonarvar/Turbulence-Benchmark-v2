def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[240:902], start=240) if x % 546 == 0 or x % 709 == 0))