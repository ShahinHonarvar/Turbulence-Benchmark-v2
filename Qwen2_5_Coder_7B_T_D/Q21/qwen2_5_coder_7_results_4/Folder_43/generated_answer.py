def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst, start=1) if 10 <= i <= 37 and num % -64 == 0]