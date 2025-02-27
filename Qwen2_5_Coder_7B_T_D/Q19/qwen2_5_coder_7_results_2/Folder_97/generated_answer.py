def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 14 < i < 48 and num % 16 != 0]