def all_ints_div_by_both_two_nums(int_list):
    return [num for num in int_list[80:201] if num % 10 == 0 and num % 1000 == 0]