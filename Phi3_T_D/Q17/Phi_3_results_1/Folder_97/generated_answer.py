def all_ints_div_by_both_two_nums(integers):
    start_index = 58
    end_index = 75
    return [num for num in integers[start_index:end_index + 1] if num % 72 == 0 and num % 62 == 0]