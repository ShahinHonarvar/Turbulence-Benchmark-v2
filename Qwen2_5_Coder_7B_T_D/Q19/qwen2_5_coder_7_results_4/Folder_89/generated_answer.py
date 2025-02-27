def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 48 < i < 62 and num % 28 != 0]