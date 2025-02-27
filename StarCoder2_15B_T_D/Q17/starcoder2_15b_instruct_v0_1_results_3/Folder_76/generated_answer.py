def all_ints_div_by_both_two_nums(input_list):
    return [x for i, x in enumerate(input_list) if i >= 250 and i <= 629 and (x % 850 == 0) and (x % 587 == 0)]