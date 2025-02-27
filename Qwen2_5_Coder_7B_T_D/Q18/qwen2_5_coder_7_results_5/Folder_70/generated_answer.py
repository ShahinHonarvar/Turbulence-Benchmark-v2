def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[42:44]) if x % 15 == 0 or x % 87 == 0))