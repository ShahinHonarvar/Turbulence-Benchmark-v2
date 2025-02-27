def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[31:51]) if x % 81 == 0 or x % 64 == 0))