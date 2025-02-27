def all_ints_div_by_both_two_nums(ints_list):
    return [x for i, x in enumerate(ints_list[12:19], start=13) if x % 45 == 0 and x % 20 == 0]