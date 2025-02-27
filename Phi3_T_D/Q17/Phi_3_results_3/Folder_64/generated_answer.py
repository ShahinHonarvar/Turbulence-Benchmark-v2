def all_ints_div_by_both_two_nums(integers_list):
    return [x for x in integers_list[:4] if x % 11 == 0 and x % -7 == 0]