def sum_ints_div_by_either_nums(int_list):
    sum_result = sum((num for num in int_list[25:81] if num % -20 == 0 or num % -26 == 0))
    return sum_result