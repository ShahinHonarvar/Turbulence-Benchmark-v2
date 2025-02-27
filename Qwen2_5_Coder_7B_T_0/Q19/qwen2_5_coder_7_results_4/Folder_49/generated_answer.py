def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 80 < i < 200 and num % 1000 != 0]