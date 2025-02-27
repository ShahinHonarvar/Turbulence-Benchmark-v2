def all_ints_div_by_both_two_nums(int_list):
    start_index = 78
    end_index = 81
    result = [num for num in int_list[start_index:end_index + 1] if num % 76 == 0 and num % 60 == 0]
    return result