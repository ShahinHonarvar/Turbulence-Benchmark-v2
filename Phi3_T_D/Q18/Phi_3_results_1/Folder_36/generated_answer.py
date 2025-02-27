def sum_ints_div_by_either_nums(lst):
    start_index, end_index = (299, 382)
    divisors = [858, 952]
    return sum((x for i, x in enumerate(lst[start_index:end_index + 1], start_index) if any((x % d == 0 for d in divisors))))