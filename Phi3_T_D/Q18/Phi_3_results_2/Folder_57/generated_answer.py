def sum_ints_div_by_either_nums(int_list):
    sum_result = sum((num for num in int_list[51:77] if num % -90 == 0 or num % -59 == 0))
    return sum_result