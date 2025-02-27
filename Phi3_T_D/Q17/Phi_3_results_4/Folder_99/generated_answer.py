def all_ints_div_by_both_two_nums(int_list):
    start, end = (154, 798)
    return [num for num in int_list[start:end + 1] if num % 275 == 0 and num % 580 == 0]