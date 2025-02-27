def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst[10:53], start=10) if num % -12 == 0]