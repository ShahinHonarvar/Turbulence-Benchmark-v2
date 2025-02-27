def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 10 < i < 100 and num % 100 != 0]