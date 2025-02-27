def all_ints_div_by_both_two_nums(int_list):
    range_start, range_end = (48, 59)
    divisors = [88, 58]
    result = [num for num in int_list[range_start:range_end + 1] if all((num % divisor == 0 for divisor in divisors))]
    return result