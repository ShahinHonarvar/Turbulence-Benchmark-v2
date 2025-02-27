def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst, start=1) if 12 <= i <= 77 and num % -19 == 0]