def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[:7] if num % -5 == 0 or num % -6 == 0))