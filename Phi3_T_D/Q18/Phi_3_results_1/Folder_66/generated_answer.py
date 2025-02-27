def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[58:82] if num % 55 == 0 or num % 10 == 0))