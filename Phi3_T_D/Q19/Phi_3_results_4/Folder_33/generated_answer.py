def all_ints_not_div_by_num(lst):
    start = 103
    end = 574
    return [x for x in lst[start:end] if x % -514 != 0]