def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 16 < i < 87 and num % -15 != 0]