def all_ints_div_by_both_two_nums(integers_list):
    start, end = (41, 56)
    return [num for num in integers_list[start:end + 1] if num % 82 == 0 and num % 90 == 0]