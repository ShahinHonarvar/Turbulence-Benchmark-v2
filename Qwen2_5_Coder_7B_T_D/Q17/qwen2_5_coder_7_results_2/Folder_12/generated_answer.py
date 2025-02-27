def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[35:65]) if x % -30 == 0 and x % -95 == 0]