def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[31:51] if num % 81 == 0 or num % 64 == 0))