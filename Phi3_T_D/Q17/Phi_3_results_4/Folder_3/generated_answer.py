def all_ints_div_by_both_two_nums(int_list):
    divisible_elements = [x for x in int_list[28:34] if x % -41 == 0 and x % -47 == 0]
    return divisible_elements