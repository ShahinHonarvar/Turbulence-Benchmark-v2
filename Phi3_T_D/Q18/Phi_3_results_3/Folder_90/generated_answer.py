def sum_ints_div_by_either_nums(int_list):
    start, end = (138, 424)
    divisors = [-863, -329]
    total = sum((val for i, val in enumerate(int_list) if start <= i <= end and any((val % d == 0 for d in divisors))))
    return total