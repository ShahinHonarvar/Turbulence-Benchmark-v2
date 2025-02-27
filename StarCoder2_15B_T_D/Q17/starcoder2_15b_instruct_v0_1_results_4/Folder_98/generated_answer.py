def all_ints_div_by_both_two_nums(ints_list):
    return [x for x in ints_list[0:6] if x % -1 == 0 and x % 13 == 0]