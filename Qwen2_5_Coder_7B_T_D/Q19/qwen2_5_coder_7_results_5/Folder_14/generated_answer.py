def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 2 < i < 8 and num % 8 != 0]