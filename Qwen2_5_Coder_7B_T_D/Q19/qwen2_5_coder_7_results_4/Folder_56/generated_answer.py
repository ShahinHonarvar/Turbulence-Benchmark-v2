def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 7 < i < 9 and num % -9 != 0]