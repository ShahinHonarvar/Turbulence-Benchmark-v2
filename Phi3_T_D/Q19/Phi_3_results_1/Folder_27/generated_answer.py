def all_ints_not_div_by_num(lst):
    start, end = (14, 21)
    return [x for x in lst[start:end] if x % -93 != 0]