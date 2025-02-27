def all_ints_div_by_both_two_nums(int_list):
    multi_of_546_and_709 = [num for num in int_list[240:902] if num % 546 == 0 and num % 709 == 0]
    return multi_of_546_and_709