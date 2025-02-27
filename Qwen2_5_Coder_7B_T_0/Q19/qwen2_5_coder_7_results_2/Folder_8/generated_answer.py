def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 17 < i < 88 and num % -75 != 0]