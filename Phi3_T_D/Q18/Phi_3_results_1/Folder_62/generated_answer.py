def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[44:59 + 1] if num % 39 == 0 or num % 15 == 0))