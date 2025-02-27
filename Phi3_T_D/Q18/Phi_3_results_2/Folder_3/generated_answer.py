def sum_ints_div_by_either_nums(int_list):
    sum_of_divisible = sum((num for num in int_list[38:53] if num % -41 == 0 or num % -47 == 0))
    return sum_of_divisible