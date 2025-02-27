def all_ints_div_by_both_two_nums(lst):
    start_index = 55
    end_index = 84
    return [num for num in lst[start_index:end_index + 1] if num % -24 == 0 and num % -11 == 0]