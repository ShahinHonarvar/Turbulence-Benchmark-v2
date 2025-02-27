def all_ints_div_by_both_two_nums(int_list):
    start_idx = 61
    end_idx = min(88, len(int_list))
    return [num for num in int_list[start_idx:end_idx + 1] if num % 31 == 0 and num % 11 == 0]