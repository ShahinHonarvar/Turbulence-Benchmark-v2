def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst[42:98], 42) if x % 46 == 0]