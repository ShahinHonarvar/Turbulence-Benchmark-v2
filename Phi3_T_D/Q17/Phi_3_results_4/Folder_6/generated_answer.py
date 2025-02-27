def all_ints_div_by_both_two_nums(int_list):
    valid_ints = [num for num in int_list[41:57] if num % 82 == 0 and num % 90 == 0]
    return valid_ints