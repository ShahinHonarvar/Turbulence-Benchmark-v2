def all_ints_div_by_both_two_nums(int_list):
    start, end = (25, 95)
    divisor = 51 * 77
    return [n for i, n in enumerate(int_list[start:end + 1], start) if n % divisor == 0]