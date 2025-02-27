def all_ints_div_by_both_two_nums(lst):
    return [x for x in filter(lambda x: all([x % -30 == 0, x % -88 == 0]), lst)][57:85]