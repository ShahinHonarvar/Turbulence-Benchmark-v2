def all_ints_div_by_both_two_nums(int_list):
    start, end = (58, 75)
    result = [num for num in int_list[start:end + 1] if num % 72 == 0 and num % 62 == 0]
    return result