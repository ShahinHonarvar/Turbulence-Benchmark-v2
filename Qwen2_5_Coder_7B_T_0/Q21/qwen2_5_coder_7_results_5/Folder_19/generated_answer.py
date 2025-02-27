def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst) if 1 <= i <= 8 and num % 6 == 0]