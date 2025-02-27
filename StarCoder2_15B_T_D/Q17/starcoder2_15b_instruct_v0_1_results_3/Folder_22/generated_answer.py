def all_ints_div_by_both_two_nums(integers_list):
    return [num for index, num in enumerate(integers_list) if 40 <= index <= 200 and num % 21 == 0 and (num % 71 == 0)]