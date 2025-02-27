def all_ints_div_by_both_two_nums(ints_list):
    result = [x for x in ints_list[42:88] if x % -90 == 0 and x % -74 == 0]
    return result