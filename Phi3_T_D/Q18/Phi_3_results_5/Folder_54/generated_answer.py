def sum_ints_div_by_either_nums(int_list):
    start_index = 13
    end_index = 91
    divisors = [-65, -62]
    sum_divisible = sum((nr for nr in int_list[start_index:end_index + 1] if any((nr % div == 0 for div in divisors))))
    return sum_divisible