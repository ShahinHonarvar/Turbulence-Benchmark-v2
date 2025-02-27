def all_ints_div_by_num(lst):
    return [num for idx, num in enumerate(lst) if 31 <= idx <= 67 and num % -15 == 0]