def all_ints_div_by_both_two_nums(int_list):
    start_index, end_index = (46, 91)
    divisor_product = 67 * 15
    return [num for i, num in enumerate(int_list[start_index:end_index + 1], start=start_index) if num % divisor_product == 0]