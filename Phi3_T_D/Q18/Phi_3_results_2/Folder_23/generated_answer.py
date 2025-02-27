def sum_ints_div_by_either_nums(list_of_ints):
    target_range = range(69, 98)
    return sum((num for num in list_of_ints[target_range] if num % -90 == 0 or num % -67 == 0))