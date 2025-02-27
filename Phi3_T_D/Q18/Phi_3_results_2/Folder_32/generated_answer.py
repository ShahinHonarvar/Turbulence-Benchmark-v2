def sum_ints_div_by_either_nums(int_list):
    total = sum((num for num in int_list[25:96] if num % 51 == 0 or num % 77 == 0))
    return total