def sum_ints_div_by_either_nums(int_list):
    target_sum = sum((num for num in int_list[18:53] if num % 15 == 0 or num % 57 == 0))
    return target_sum