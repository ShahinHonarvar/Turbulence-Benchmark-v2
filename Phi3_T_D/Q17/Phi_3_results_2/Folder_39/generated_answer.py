def all_ints_div_by_both_two_nums(lst):
    start_index, end_index = (13, 76)
    result = [num for num in lst[start_index:end_index + 1] if num % -66 == 0 and num % -32 == 0]
    return result