def sum_ints_div_by_either_nums(lst):
    if len(lst) < 98:
        return 0
    return sum((x for x in lst[69:98] if x % -90 == 0 or x % -67 == 0))