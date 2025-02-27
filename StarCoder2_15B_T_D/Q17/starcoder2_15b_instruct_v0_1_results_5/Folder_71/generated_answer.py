def all_ints_div_by_both_two_nums(ints_list):
    return [int for idx, int in enumerate(ints_list) if int % -37 == 0 and int % -26 == 0 and (68 <= idx <= 99)]