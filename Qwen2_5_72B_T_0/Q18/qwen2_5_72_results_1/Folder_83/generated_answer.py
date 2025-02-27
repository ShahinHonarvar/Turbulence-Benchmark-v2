def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[90:201], start=90) if x % -31 == 0 or x % 13 == 0))