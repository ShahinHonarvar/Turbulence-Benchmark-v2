def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[42:88], start=42) if x % -90 == 0 or x % -74 == 0))