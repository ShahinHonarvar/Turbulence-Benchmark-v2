def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list[:3] if num % -2 == 0 and num % 3 == 0]