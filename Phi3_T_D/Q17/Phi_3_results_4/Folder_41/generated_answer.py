def all_ints_div_by_both_two_nums(int_list):
    result = [num for num in int_list[0:10] if num % 6 == 0 and num % -3 == 0]
    return result