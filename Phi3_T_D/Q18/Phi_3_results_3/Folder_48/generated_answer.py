def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[306:958] if num % 982 == 0 or num % 319 == 0))