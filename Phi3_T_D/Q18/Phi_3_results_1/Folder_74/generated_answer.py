def sum_ints_div_by_either_nums(number_list):
    sum_divisible = sum((num for num in number_list[90:98] if num % 13 == 0 or num % 35 == 0))
    return sum_divisible