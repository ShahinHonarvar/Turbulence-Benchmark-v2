def all_ints_div_by_both_two_nums(int_list):
    start, end = (68, 99)
    return [num for num in int_list[start:end + 1] if num % -37 == 0 and num % -26 == 0]