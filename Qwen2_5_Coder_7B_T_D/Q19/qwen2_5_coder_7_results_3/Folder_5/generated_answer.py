def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 1 < i < 3 and num % 8 != 0]