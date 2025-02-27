def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[30:201] if num % -115 == 0 or num % 115 == 0))