def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list[:6] if num % -1 == 0 and num % 13 == 0]