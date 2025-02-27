def all_ints_div_by_num(lst):
    return [num for i, num in enumerate(lst, start=1) if i in range(18, 94) and num % -85 == 0]