def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 19 < i < 94 and num % -32 != 0]