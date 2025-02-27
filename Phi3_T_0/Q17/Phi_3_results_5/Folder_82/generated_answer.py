def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list[20:201] if num % -20 == 0 and num % -200 == 0]