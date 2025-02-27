def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 10 < i < 55 and num % 36 != 0]