def sum_ints_div_by_either_nums(int_list):
    start_index = 10
    end_index = 79
    divisors = [-74, -58]
    sum_div_ints = sum((val for idx, val in enumerate(int_list[start_index:end_index + 1], start=start_index) if any((val % div == 0 for div in divisors))))
    return sum_div_ints