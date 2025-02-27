def all_ints_not_div_by_num(lst):
    result = [value for idx, value in enumerate(lst[4:8], start=4) if value % -6 != 0]
    return result