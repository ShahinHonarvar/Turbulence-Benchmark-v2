def sum_ints_div_by_either_nums(int_list):
    divisible_sum = sum((num for i, num in enumerate(int_list[250:629 + 1]) if num % 850 == 0 or num % 587 == 0))
    return divisible_sum