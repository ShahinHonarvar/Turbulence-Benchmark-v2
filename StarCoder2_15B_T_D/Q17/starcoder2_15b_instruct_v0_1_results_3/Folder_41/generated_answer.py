def all_ints_div_by_both_two_nums(ints_list):
    return [x for x in ints_list[0:10] if x % 6 == 0 and x % -3 == 0]