def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 50 < i < 81 and num % 64 != 0]