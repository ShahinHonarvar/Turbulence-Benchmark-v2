def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 13 < i < 76 and num % 44 != 0]