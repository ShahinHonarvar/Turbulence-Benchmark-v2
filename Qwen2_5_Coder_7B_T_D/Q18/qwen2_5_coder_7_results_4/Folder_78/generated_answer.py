def sum_ints_div_by_either_nums(num_list):
    return sum((num for i, num in enumerate(num_list[34:70]) if num % 19 == 0 or num % 32 == 0))