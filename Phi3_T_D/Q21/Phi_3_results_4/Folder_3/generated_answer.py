def all_ints_div_by_num(lst):
    start, end = (25, 59)
    return [x for x in lst[start:end + 1] if x % -26 == 0]