def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[69:98]
    return sum((num for num in target_range if num % -90 == 0 or num % -67 == 0))