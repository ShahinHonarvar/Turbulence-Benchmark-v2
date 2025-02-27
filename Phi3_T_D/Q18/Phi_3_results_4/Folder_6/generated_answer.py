def sum_ints_div_by_either_nums(int_list):
    start_index, end_index = (41, 56)
    divisors = [82, 90]
    return sum((x for i, x in enumerate(int_list[start_index:end_index + 1]) if any((x % d == 0 for d in divisors))))