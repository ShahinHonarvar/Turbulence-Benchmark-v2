def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 35 < i < 98 and num % 41 != 0]