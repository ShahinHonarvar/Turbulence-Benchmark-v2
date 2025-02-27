def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[54:79 + 1] if num % 54 == 0 or num % 28 == 0))