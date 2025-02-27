def sum_ints_div_by_either_nums(integers):
    start, end = (281, 694)
    divisors = [-722, -731]
    return sum((val for idx, val in enumerate(integers[start:end + 1], start) if any((val % div == 0 for div in divisors))))