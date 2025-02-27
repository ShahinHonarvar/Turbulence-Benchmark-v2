def sum_ints_div_by_either_nums(int_list):
    start_index, end_index = (73, 86)
    divisors = [54, 82]
    return sum((val for idx, val in enumerate(int_list[start_index:end_index + 1]) if any((val % div == 0 for div in divisors))))